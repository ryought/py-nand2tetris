#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Parser:
    def __init__(self, f):
        self.f = f  # file path
        # self.command = f.readline() # 今のコマンド 1lineがそのまま入る
        self.command = ''
        self.finished = False
        self.advance()

    def commandType(self):
        token = self.command.split()
        if token[0][0] == '@':
            # シンボルor即値
            return 'A_COMMAND'
        elif token[0][0] == '(' and token[-1][-1] == ')':
            # 擬似コマンド
            return 'L_COMMAND'
        else:
            # 計算命令
            return 'C_COMMAND'

    # ファイル読み込み関連
    def hasMoreCommands(self):
        # TODO やばい
        return self.finished

    def advance(self):
        while True:
            line = self.f.readline()
            if line == '':
                # EOF
                self.finished = True
                break
            if not line.startswith('//') and not line.startswith('\n'):
                self.command = line
                break

    # コマンドからニモニックを返す関数
    def symbol(self):
        token = self.command.split()[0]
        if token[0] == '@':
            return token[1:] # 最初の文字以外
        elif token[0] == '(':  # ラベルシンボル
            return token[1:-1]
        else:
            return 'error'

    def dest(self):
        cmd = self.command.split()[0]
        if '=' in cmd:
            i = cmd.find('=')
            return cmd[:i]  # =より前を返す
        else:
            # = not exists
            return 'null'

    def comp(self):
        cmd = self.command.split()[0]
        i = cmd.find('=')
        j = cmd.find(';')
        if i == -1:
            if j == -1:
                return cmd
            else:
                return cmd[:j]
        else:
            if j == -1:
                return cmd[i+1:]
            else:
                return cmd[i+1:j]  # =と;の間を返す

    def jump(self):
        cmd = self.command.split()[0]
        if ';' in cmd:
            i = cmd.find(';')
            return cmd[i+1:]
        else:
            return 'null'

def main():
    with open('test/add/Add.asm', 'r') as f:
        c = Parser(f)
        while not c.hasMoreCommands():
            c.advance()
            print('[cmd]:', c.command)
        print('finished')
main()
