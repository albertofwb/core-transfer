import asyncio
import signal
from web3 import AsyncWeb3
from web3.exceptions import BlockNotFound
from web3.middleware import async_geth_poa_middleware
from abi import CORE_RPC_URL
from core_wallet import CoreWallet
from private import to_address, monitor_wallets
from util import get_wallet_address_from_private_key
from log_utils import get_logger

logger = get_logger(__name__)


class Monitor:
    def __init__(self, private_keys: [str]):
        self.private_keys = private_keys
        self.w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(CORE_RPC_URL))
        self.w3.middleware_onion.inject(async_geth_poa_middleware, layer=0)
        self.private_map_address = self.construct_addresses()
        self.is_running = True

    def construct_addresses(self):
        address_map = {}
        for i in self.private_keys:
            from_address = get_wallet_address_from_private_key(i)
            address_map[from_address] = i
        return address_map

    async def transfer_all(self, private_key, to_address):
        wallet = CoreWallet(private_key)
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, wallet.quick_transfer_all_with_high_gas, to_address)

    async def handle_transaction(self, tx):
        wei = tx['value']
        core = self.w3.from_wei(wei, 'ether')
        gas = self.w3.from_wei(tx['gasPrice'] * tx['gas'], 'ether')
        if core > 10:
            logger.debug(
                f"txf={gas:,.5f}: {tx['from']} => {tx['to']} {core} https://scan.coredao.org/tx/{self.w3.to_hex(tx['hash'])}")
        if tx['to'] in self.private_map_address:
            private_key = self.private_map_address[tx['to']]
            try:
                await self.transfer_all(private_key, to_address)
            except Exception as ex:
                logger.warning(f"转账失败: {tx['to']} => {to_address}", exc_info=ex)

    async def monitor_transactions(self):
        monitor_addresses = self.private_map_address.keys()
        logger.info(f"开始监控地址 {monitor_addresses} 的交易...")
        last_block = await self.w3.eth.get_block_number()
        while self.is_running:
            try:
                current_block = await self.w3.eth.get_block_number()
                for block_number in range(last_block + 1, current_block + 1):
                    try:
                        block = await self.w3.eth.get_block(block_number, full_transactions=True)
                    except BlockNotFound:
                        await asyncio.sleep(1)
                        continue
                    for tx in block.transactions:
                        if not self.is_running:
                            break
                        await self.handle_transaction(tx)
                    logger.debug(f"Processed {len(block.transactions):2d} transactions of block {current_block} https://scan.coredao.org/txs?block={current_block}")
                last_block = current_block
                await asyncio.sleep(1)  # Wait for 1 second before checking again
            except Exception as e:
                logger.error(f"An error occurred: {e}", exc_info=e)
                await asyncio.sleep(5)  # Wait for 5 seconds before retrying

        logger.info("监控已停止")

    def stop(self):
        self.is_running = False
        logger.info("正在停止监控...")


async def main():
    monitor = Monitor(monitor_wallets)

    def signal_handler(_, _2):
        logger.info("接收到停止信号，正在优雅退出...")
        monitor.stop()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    await monitor.monitor_transactions()


if __name__ == '__main__':
    asyncio.run(main())