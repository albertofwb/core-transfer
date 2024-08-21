import asyncio
from web3 import AsyncWeb3
from web3.exceptions import BlockNotFound
from web3.middleware import async_geth_poa_middleware
from abi import MIN_GAS_PRICE, CORE_RPC_URL
from core_wallet import CoreWallet
from private import to_address, monitor_wallets
from util import get_wallet_address_from_private_key


class Monitor:
    def __init__(self, private_keys: [str]):
        self.private_keys = private_keys
        self.w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(CORE_RPC_URL))
        self.w3.middleware_onion.inject(async_geth_poa_middleware, layer=0)
        self.private_map_address = self.construct_addresses()

    def construct_addresses(self):
        address_map = {}
        for i in self.private_keys:
            from_address = get_wallet_address_from_private_key(i)
            address_map[from_address] = i
        return address_map

    async def transfer(self, private_key, to_address, amount):
        wallet = CoreWallet(private_key)
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, wallet.transfer, to_address, amount, False)

    async def monitor_transactions(self):
        monitor_addresses = self.private_map_address.keys()
        print(f"开始监控地址 {monitor_addresses} 的交易...")
        last_block = await self.w3.eth.get_block_number()
        try:
            while True:
                current_block = await self.w3.eth.get_block_number()

                for block_number in range(last_block + 1, current_block + 1):
                    try:
                        block = await self.w3.eth.get_block(block_number, full_transactions=True)
                    except BlockNotFound:
                        await asyncio.sleep(1)
                        continue
                    for tx in block.transactions:
                        if tx['to'] in monitor_addresses:
                            private_key = self.private_map_address[tx['to']]
                            amount = float(self.w3.from_wei(tx['value'], 'ether')) - MIN_GAS_PRICE
                            try:
                                await self.transfer(private_key, to_address, amount)
                            except Exception as ex:
                                print(f"转账失败: {tx['to']} => {to_address} {amount} CORE", ex)
                last_block = current_block
                await asyncio.sleep(1)  # Wait for 1 second before checking again
        except KeyboardInterrupt:
            print("监控已停止")


async def main():
    monitor = Monitor(monitor_wallets)
    await monitor.monitor_transactions()


if __name__ == '__main__':
    asyncio.run(main())
