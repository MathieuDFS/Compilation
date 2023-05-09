import sys

from NavalWargaming.Compiler.NavalWargamingLexer import NavalWargamingLexer
from NavalWargaming.Compiler.NavalWargamingParser import NavalWargamingParser
from NavalWargaming.Compiler.PrettyPrinter import PrettyPrinter
from NavalWargaming.Compiler.SemanticVisitor import SemanticVisitor

if __name__ == "__main__":
    PrettyPrint =False
    if(len(sys.argv) == 3):
        PrettyPrint = True
        prettyPrintName = sys.argv[2]
    elif (len(sys.argv) != 2):
        print("Usage: python main.py <file_name>")
        print("Or: python main.py <file_name> <pretty_print_name>")
        print("Example: python main.py ../examples/unit_exemple3.nwg")
        exit(1)

    filename = sys.argv[1]

    L = NavalWargamingLexer()
    parser = NavalWargamingParser(L.lex_file(filename))
    AST = parser.parse()
    semanticVisitor = SemanticVisitor()
    semanticVisitor.visit(AST)
    wargame = semanticVisitor.InitializeWargame()

    if (PrettyPrint):
        PrettyPrint = PrettyPrinter()
        PrettyPrint.visit(AST,prettyPrintName)

    wargame.run()



