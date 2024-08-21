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
