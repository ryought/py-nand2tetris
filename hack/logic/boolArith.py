# 絶対参照で書いた場合
from hack.logic.boolLogic import And
# パッケージ内相対参照の時は以下
# from . import boolLogic
# 参照: https://docs.python.jp/3/tutorial/modules.html
# http://docs.python-guide.org/en/latest/writing/structure/#structure-of-the-repository

def print_And():
    print(And(1,1))


if __name__ == '__main__':
    print_And()

