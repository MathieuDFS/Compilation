NWG_LEXEM_REGEXES = [
    #backline and tabulations
    # (r" ", "TAB"),
    # (r"\r", "BACKLINE"),
    # Comments and whitespaces
    (r"#.*", None),
    (r"[ \t\n]+", None),
    # Special character
    (r"\:", "COLON"),

    (r"\*", "MULT"),
    # Keywords
    (r"Fleets", "KW_FLEETS"),
    (r"fleet", "KW_FLEET"),
    (r"Factions", "KW_FACTIONS"),
    (r"Relations", "KW_RELATIONS"),
    (r"Map", "KW_MAP"),
    # Variables
    (r"[+-]?[0-9]+", "INT"),
    (r"\-", "MINUS"),
    (r"[a-zA-Z0-9_]*", "IDENT"), #todo accepté les espaces

    ]