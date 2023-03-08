NWG_LEXEM_REGEXES = [
    # Comments and whitespaces
    (r"#.*", None),
    (r"[ \t\n]+", None),
    # Special characters and backlines
    (r"\:", "COLON"),
    (r"\-", "MINUS"),
    # Keywords
    (r"fleets", "KW_FLEETS"),
    (r"fleet", "KW_FLEET"),
    (r"factions", "KW_FACTIONS"),
    (r"relations", "KW_RELATIONS"),
    # Variables
    (r"[+-]?[0-9]+", "INT"),
    (r"[a-zA-Z0-9_]*", "IDENT"), #todo accepté les espaces

    ]