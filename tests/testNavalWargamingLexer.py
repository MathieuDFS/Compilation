# -*- encoding: utf-8 -*-

import pytest

from Compiler.NavalWargamingLexer import NavalWargamingLexem, NavalWargamingLexer



@pytest.mark.parametrize("test_program", ["unit_exemple1.nwg", "unit_exemple2.nwg", "unit_exemple3.nwg", "unit_exemple4.nwg"])
def test_lex_complete(test_program):
    lexer = NavalWargamingLexer()
    lexer.lex_file("../examples/" + test_program)

