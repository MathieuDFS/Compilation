from Compiler.NavalWargamingLexer import NavalWargamingLexer
from Compiler.NavalWargamingParser import NavalWargamingParser
from NavalWargaming.Compiler.PrettyPrinter import PrettyPrinter
from NavalWargaming.Compiler.SemanticVisitor import SemanticVisitor

if __name__ == "__main__":
    L = NavalWargamingLexer()
    parser = NavalWargamingParser(L.lex_file("../examples/unit_exemple3.nwg"))
    AST = parser.parse()
    semanticVisitor = SemanticVisitor()
    semanticVisitor.visit(AST)
    wargame = semanticVisitor.InitializeWargame()
    PrettyPrint = PrettyPrinter()
    PrettyPrint.visit(AST,"Example4")



