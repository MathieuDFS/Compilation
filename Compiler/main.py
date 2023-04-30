from Compiler.NavalWargamingLexer import NavalWargamingLexem, NavalWargamingLexer
from Compiler.NavalWargamingParser import NavalWargamingParser
from PrettyPrinter import PrettyPrinter
from EmptyVisitor import EmptyVisitor

if __name__ == "__main__":
    L = NavalWargamingLexer()
    print(L.lex_file("../examples/unit_exemple2.nwg"))
    print("Parsing...")
    parser = NavalWargamingParser(L.lex_file("../examples/unit_exemple2.nwg"))
    AST = parser.parse()
    print("parse done")
    EmptyVisitor = EmptyVisitor()
    EmptyVisitor.visit(AST)
    print("First visit done")
    PrettyPrint = PrettyPrinter()
    PrettyPrint.visit(AST)



