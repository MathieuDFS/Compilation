import logging
from Compiler.NavalWargamingAbstractSyntax import *

logger = logging.getLogger(__name__)

class ParsingException(Exception):
    pass

class NavalWargamingParser:
    def __init__(self, lexems):
        """
        Component in charge of syntaxic analysis.
        """
        self.lexems = lexems

    # ==========================
    #      Helper Functions
    # ==========================

    def accept(self):
        """
        Pops the lexem out of the lexems list.
        """
        self.show_next()
        return self.lexems.pop(0)

    def show_next(self, n=1):
        """
        Returns the next token in the list WITHOUT popping it.
        """
        try:
            return self.lexems[n - 1]
        except IndexError:
            self.error("No more lexems left.")

    def expect(self, tag):
        """
        Pops the next token from the lexems list and tests its type through the tag.
        """
        next_lexem = self.show_next()
        if next_lexem.tag != tag:
            raise ParsingException(
                f"ERROR at {str(self.show_next().position)}: Expected {tag}, got {next_lexem.tag} instead"
            )
        return self.accept()

    def remove_comments(self):
        """
        Removes the comments from the token list by testing their tags.
        """
        self.lexems = [lexem for lexem in self.lexems if lexem.tag != "COMMENT"]

    # ==========================
    #     Parsing Functions
    # ==========================

    def parse(self):
        """
        Main function: launches the parsing operation given a lexem list.
        """
        try:
            self.remove_comments()
            self.parse_program()
        except ParsingException as err:
            logger.exception(err)
            raise

    def parse_program(self):
        AST = Abstract_Syntax_Tree()
        FactionsTree = None
        RelationsTree = None
        FleetsTree = None

        if(self.show_next().tag == "KW_FACTIONS"):
            print("Factions")
            self.expect("KW_FACTIONS")
            self.expect("COLON")
            factionList = []
            while (self.show_next().tag == "MINUS"):
                faction = self.parse_faction()
                factionList.append(faction)
            FactionsTree = Factions(factionList)

        if(self.show_next().tag == "KW_RELATIONS"):
            print("Relations")
            self.expect("KW_RELATIONS")
            self.expect("COLON")
            relationList = []
            while (self.show_next().tag == "MINUS"):
                relation = self.parse_relation()
                relationList.append(relation)
            RelationsTree = Relations(relationList)

        AST=Program(Initial_State(FactionsTree,RelationsTree,FleetsTree,None),[])

    def parse_faction(self):
        print("Faction")
        self.expect("MINUS")
        faction = Faction(self.parse_identifier())
        return faction

    def parse_relation(self):
        print("Relation")
        self.expect("MINUS")
        faction1 = self.parse_identifier()
        self.expect("MINUS")
        faction2 = self.parse_identifier()
        self.expect("COLON")
        relation = self.show_next().value
        print(self.show_next().value)
        self.expect("INT")
        return Relation(faction1,faction2,relation)

    def parse_identifier(self):
        ident = Identifier(self.show_next().value)
        print(ident.name)
        self.expect("IDENT")
        return ident

    # ==============================
    #     Starter tests Functions
    # ==============================