from Compiler.NavalWargamingLexer import NavalWargamingLexem, NavalWargamingLexer
from Compiler.NavalWargamingParser import NavalWargamingParser

if __name__ == "__main__":
    L = NavalWargamingLexer()
    print(L.lex_file("../examples/unit_exemple2.nwg"))
    print("Parsing...")
    parser = NavalWargamingParser(L.lex_file("../examples/unit_exemple2.nwg"))
    AST = parser.parse()
    print("parse done")


