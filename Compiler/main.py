from Compiler.NavalWargamingLexer import NavalWargamingLexem, NavalWargamingLexer

if __name__ == "__main__":
    L = NavalWargamingLexer()
    print(L.lex_file("../examples/unit_exemple4.nwg"))


