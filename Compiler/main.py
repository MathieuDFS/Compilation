from Compiler.NavalWargamingLexer import NavalWargamingLexem, NavalWargamingLexer
from Compiler.NavalWargamingParser import NavalWargamingParser
from PrettyPrinter import PrettyPrinter
from SemanticVisitor import SemanticVisitor



if __name__ == "__main__":
    L = NavalWargamingLexer()
    # print(L.lex_file("../examples/unit_exemple2.nwg"))
    print("Parsing...")
    parser = NavalWargamingParser(L.lex_file("../examples/unit_exemple3.nwg"))
    AST = parser.parse()
    print("parse done")
    semanticVisitor = SemanticVisitor()
    semanticVisitor.visit(AST)
    wargame = semanticVisitor.InitializeWargame()
    print("First visit done")
    PrettyPrint = PrettyPrinter()
    PrettyPrint.visit(AST,"Example4")



