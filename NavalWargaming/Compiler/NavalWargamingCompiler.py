


class NavalWargamingCompiler():
    def __init__(self):
        self.lexer = NavalWargamingLexer()
        self.parser = NavalWargamingParser()


    def compile(self, code):
        code_lexer = lexer.lex_file(code)
        AST = parser.parse(code_lexer)
        