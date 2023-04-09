import os
import sys


def greeting_path(msg, name):
    print(sys.argv)
    os.get_exec_path()
    print(f"{msg}, {name}")


def print_hi(name) -> None:
    # スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
    print(f'Hi, {name}')  # Ctrl+F8を押すとブレークポイントを切り替えます。


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    print_hi('PyCharm')

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
