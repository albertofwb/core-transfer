from core_wallet import CoreWallet, transaction_callback
from private import private_key, to_address

if __name__ == '__main__':
    wallet = CoreWallet(private_key)
    wallet.get_core_balance(to_address)
    wallet.monitor_transactions(transaction_callback)
