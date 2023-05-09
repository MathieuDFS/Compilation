import sys

from Compiler.NavalWargamingLexer import NavalWargamingLexer
from Compiler.NavalWargamingParser import NavalWargamingParser
from Compiler.PrettyPrinter import PrettyPrinter
from Compiler.SemanticVisitor import SemanticVisitor

if __name__ == "__main__":
    IDE = False # Set to True if you want to run the program in the IDE
    PrettyPrint = False

    if IDE:
        filename = "../examples/unit_exemple3.nwg" # Change this line to run another file
        PrettyPrint = False # Set to True if you want to pretty print the AST
        prettyPrintName ="exemple3" # Change this line to change the name of the pretty printed file
    else:
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



