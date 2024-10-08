from web3 import Web3
from web3.middleware import geth_poa_middleware
from abi import CORE_RPC_URL, MIN_GAS_PRICE, MAX_GAS_PRICE, GAS_LIMIT_WEI
from eth_utils import to_checksum_address
from tg_notify import tg_notify
from util import get_wallet_address_from_private_key
from log_utils import get_logger
logger = get_logger(__name__)


class CoreWallet:
    def __init__(self, private_key: str):
        self.w3 = Web3(Web3.HTTPProvider(CORE_RPC_URL))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        if not self.w3.is_connected():
            raise ConnectionError("无法连接到Core DAO网络")
        self.private_key = private_key
        self.from_address = to_checksum_address(get_wallet_address_from_private_key(private_key))
        # self.balance = float(self.get_core_balance())

    def is_valid_address(self, address):
        return self.w3.is_address(address)

    def get_core_balance(self, address=None) -> float:
        if address is None:
            address = self.from_address
        balance_wei = self.w3.eth.get_balance(address)
        balance = self.w3.from_wei(balance_wei, 'ether')
        # print(f"地址 {address} 的信息:")
        # print(f"Core余额: {balance} CORE")
        return float(balance)

    def quick_transfer_all_with_high_gas(self, to_address):
        balance = self.get_core_balance()
        # fuck the address of 0x6180931Acb68B81555C5B5d07D045B41bAc6f110
        # you take 75% as transaction fee which spent mine 2.1 test cores
        # I set up 80% as transaction fee let's see who can win
        gas = balance * 0.8
        if balance <= gas:
            raise ValueError(f"余额不足以支付gas费用 {balance} <= {gas}")
        amount = balance - gas
        if amount <= 0:
            raise ValueError("转账金额过小")
        nonce = self.w3.eth.get_transaction_count(self.from_address)
        value = self.w3.to_wei(amount, 'ether')
        gas_price = self.w3.to_wei(gas, 'ether') // GAS_LIMIT_WEI

        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': value,
            'gas': GAS_LIMIT_WEI,  # 标准转账gas限制
            'gasPrice': gas_price,  # 将总gas费用除以gas限制得到每单位gas的价格
        }

        signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        txf = self.w3.from_wei(gas_price * GAS_LIMIT_WEI, 'ether')
        logger.info(f"{self.from_address} => {to_address} {amount} CORE (Gas: {txf:,.5f} CORE)")
        logger.info(f"交易已发送: https://scan.coredao.org/tx/{self.w3.to_hex(tx_hash)}")
        tg_notify(f"{self.from_address} {amount:,.5f} CORE")
        return self.w3.to_hex(tx_hash)

    def transfer(self, to_address, amount, virify_balance=True):
        if not self.is_valid_address(to_address):
            raise ValueError(f"无效的钱包地址: {to_address}")
        if amount <= 0:
            raise ValueError("金额必须大于0")
        if virify_balance and amount > self.balance:
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
        logger.info(f"transfer {self.from_address} => {to_address} {amount} CORE")
        tg_notify(f"{self.from_address} {amount} CORE")
        return self.w3.to_hex(tx_hash)

