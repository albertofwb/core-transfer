import sys
from core_wallet import CoreWallet
from private import private_key


def main():
    if len(sys.argv) != 3:
        print("使用方法: python main.py <钱包地址> <金额>")
        sys.exit(1)
    address = sys.argv[1]
    amount = float(sys.argv[2])
    try:
        checker = CoreWallet(private_key)
        checker.transfer(address, amount)
    except ConnectionError as e:
        print(f"连接错误: {e}")
    except ValueError as e:
        print(f"输入错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    main()
