# -*- encoding: utf-8 -*-

import pytest

from Compiler.NavalWargamingLexer import NavalWargamingLexem, NavalWargamingLexer
from Compiler.NavalWargamingParser import NavalWargamingParser



@pytest.mark.parametrize("test_program", ["unit_exemple1.nwg", "unit_exemple2.nwg", "unit_exemple3.nwg", "unit_exemple4.nwg"])
def test_lex_complete(test_program):
    lexer = NavalWargamingLexer()
    lexer.lex_file("../examples/" + test_program)

@pytest.mark.parametrize("test_program", ["unit_exemple1.nwg", "unit_exemple2.nwg", "unit_exemple3.nwg", "unit_exemple4.nwg"])
def test_parse_complete(test_program):
    lexer = NavalWargamingLexer()
    lexems = lexer.lex_file("../examples/" + test_program)
    parser = NavalWargamingParser(lexems)
    parser.parse()