#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SymbolTable:
    def __init__(self):
        # table structure
        #  {'symbol'(str): 'address'(int)}
        self.table = {}

    def addEntry(self, symbol, address):
        # symbol(str), address(int)
        self.table[symbol] = address

    def contains(symbol):
        if symbol in self.table.keys():
            return True
        else:
            return False

    def getAddress(symbol):
        return self.table[symbol]
