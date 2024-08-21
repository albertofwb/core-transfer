import time
from web3 import Web3
from web3.exceptions import BlockNotFound
from web3.middleware import geth_poa_middleware
from abi import CORE_RPC_URL, PLEDGE_AGENT_ADDRESS, CORE_ABI
from eth_account import Account
from eth_utils import to_checksum_address


def get_wallet_address_from_private_key(private_key: str) -> str:
    if private_key.startswith('0x'):
        private_key = private_key[2:]

    try:
        account = Account.from_key(private_key)
        wallet_address = to_checksum_address(account.address)
        return wallet_address
    except ValueError as e:
        return f"Error: {str(e)}"


class CoreWallet:
    def __init__(self, private_key: str):
        self.w3 = Web3(Web3.HTTPProvider(CORE_RPC_URL))
        # Add PoA middleware
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.private_key = private_key
        self.from_address = to_checksum_address(get_wallet_address_from_private_key(private_key))
        if not self.w3.is_connected():
            raise ConnectionError("无法连接到Core DAO网络")
        self.balance = self.get_core_balance()

    def is_valid_address(self, address):
        return self.w3.is_address(address)

    def get_core_balance(self, address=None):
        if address is None:
            address = self.from_address
        balance_wei = self.w3.eth.get_balance(address)
        balance = self.w3.from_wei(balance_wei, 'ether')
        # print(f"地址 {address} 的信息:")
        # print(f"Core余额: {balance} CORE")
        return balance

    def transfer(self, to_address, amount):
        if not self.is_valid_address(to_address):
            raise ValueError(f"无效的钱包地址: {to_address}")
        if amount <= 0:
            raise ValueError("金额必须大于0")
        if amount > self.balance:
            raise ValueError(f"余额不足: {amount} > {self.balance:,.3f}")

        nonce = self.w3.eth.get_transaction_count(self.from_address)
        gas_price = self.w3.eth.gas_price
        value = self.w3.to_wei(amount, 'ether')

        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': value,
            'gas': 21000,  # 标准转账gas限制
            'gasPrice': gas_price,
        }

        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"{self.from_address} => {to_address} {amount} CORE")
        print(f"交易已发送: https://scan.coredao.org/tx/{self.w3.to_hex(tx_hash)}")
        return self.w3.to_hex(tx_hash)

    def monitor_transactions(self, address, callback):
        """
                Monitor real-time transactions for a specific address.

                :param address: The address to monitor
                :param callback: A function to call when a new transaction is detected
                """
        address = to_checksum_address(address)

        print(f"开始监控地址 {address} 的交易...")

        last_block = self.w3.eth.get_block_number()

        try:
            while True:
                current_block = self.w3.eth.get_block_number()

                for block_number in range(last_block + 1, current_block + 1):
                    try:
                        block = self.w3.eth.get_block(block_number, full_transactions=True)
                    except BlockNotFound:
                        time.sleep(1)
                        continue
                    for tx in block.transactions:
                        if tx['to'] == address or tx['from'] == address:
                            callback(self.w3, tx)
                last_block = current_block
                time.sleep(1)  # Wait for 1 second before checking again
        except KeyboardInterrupt:
            print("监控已停止")


def transaction_callback(w3, tx):
    print(f"{tx['from']} => {tx['to']} {w3.from_wei(tx['value'], 'ether')} CORE")
    # print(f"链接: https://scan.coredao.org/tx/{tx.hash.hex()}")