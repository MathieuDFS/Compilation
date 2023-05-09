import logging
from NavalWargaming.Compiler.NavalWargamingAbstractSyntax import *

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

    def remove_comments(self): #todo supprimer ou adapter les constants
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
            AST = self.parse_program()
            return AST
        except ParsingException as err:
            logger.exception(err)
            raise

    def parse_program(self):
        FactionsTree = None
        RelationsTree = None
        FleetsTree = None

        if(self.show_next().tag == "KW_FACTIONS"):
            self.expect("KW_FACTIONS")
            self.expect("COLON")
            factionList = []
            while (self.show_next().tag == "MINUS"):
                faction = self.parse_faction()
                factionList.append(faction)
            FactionsTree = Factions(factionList)

        if(self.show_next().tag == "KW_RELATIONS"):
            self.expect("KW_RELATIONS")
            self.expect("COLON")
            relationList = []
            while (self.show_next().tag == "MINUS"):
                relation = self.parse_relation()
                relationList.append(relation)
            RelationsTree = Relations(relationList)

        if(self.show_next().tag == "KW_FLEETS"):
            self.expect("KW_FLEETS")
            self.expect("COLON")
            fleetList = []
            while (self.show_next().tag == "MINUS"):
                fleet = self.parse_faction_fleet()
                fleetList.append(fleet)
            FleetsTree = Fleets(fleetList)

        map=self.parse_map()

        AST=Program(Initial_State(FactionsTree,RelationsTree,FleetsTree,map))
        return AST

    def parse_faction(self):
        self.expect("MINUS")
        faction = Faction(self.parse_identifier())
        return faction

    def parse_relation(self):
        self.expect("MINUS")
        faction1 = self.parse_identifier()
        self.expect("MINUS")
        faction2 = self.parse_identifier()
        self.expect("COLON")
        relation = self.show_next().value
        self.expect("INT")
        return Relation(faction1,faction2,relation)

    def parse_faction_fleet(self):
        self.expect("MINUS")
        faction = self.parse_identifier()
        self.expect("KW_FLEET")
        self.expect("COLON")
        FlotillaList = []
        while (self.starter_test_flotilla()):
            ship = self.parse_Flotilla()
            FlotillaList.append(ship)
        faction_fleet = Faction_Fleet(faction, FlotillaList)
        return faction_fleet

    def parse_Flotilla(self):
        self.expect("MINUS")
        flotilla_name = self.parse_identifier()
        self.expect("COLON")
        VesselList = []
        # Minimum 1 vessel
        vessel = self.parse_vessel()
        VesselList.append(vessel)
        while (self.show_next().tag == "INT"):
            vessel = self.parse_vessel()
            VesselList.append(vessel)
        flotilla = Flotilla(flotilla_name, VesselList)
        return flotilla

    def parse_vessel(self):
        number = self.show_next().value
        self.expect("INT")
        vessel_type = self.parse_vessel_type()
        return Vessel(number, vessel_type)

    def parse_vessel_type(self):
        vessel_type = Vessel_type(self.show_next().value)
        self.expect("IDENT")
        return vessel_type

    def parse_map(self):
        self.expect("KW_MAP")
        self.expect("COLON")
        x = self.show_next().value
        self.expect("INT")
        self.expect("MULT")
        y = self.show_next().value
        self.expect("INT")
        map = Map(x,y)
        return map

    def parse_identifier(self):
        ident = Identifier(self.show_next().value)
        self.expect("IDENT")
        return ident

    # ==============================
    #     Starter tests Functions
    # ==============================

    def starter_test_flotilla(self):
        if (self.show_next().tag == "MINUS"):
            if(self.show_next(3).tag == "COLON"):
                return True
        return False