from parser import Parser
import code
from symboltable import SymbolTable

with open('test/add/Add.asm') as f:
    parser = Parser(f)

table = SymbolTable()
table.addEntry('hoge', 12230)

