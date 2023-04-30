
class Abstract_Syntax_Tree():
    """Abstract Syntax Tree"""
    pass

class AST_Node():
    """Abstract class for AST nodes"""
    def __init__(self):
        pass

    def accept(self, visitor):
        """Accept a visitor (pattern visitor)"""
        pass



class Program(AST_Node):
    def __init__(self,initial_State, actions):
        self.initial_State: Initial_State = initial_State
        self.actions: list[Action] = actions

    def accept(self, visitor):
        visitor.visitProgram(self)


class Initial_State(AST_Node):
    def __init__(self, factions, relations, fleets,map):
        self.factions: Factions = factions
        self.relations: Relations = relations
        self.fleets: Fleets = fleets
        self.map: Map = map

    def accept(self, visitor):
        visitor.visitInitial_State(self)

class Action(AST_Node):
    pass # TODO

class Factions(AST_Node):
    def __init__(self, faction_list):
        self.faction_list: list[Faction] = faction_list

    def accept(self, visitor):
        visitor.visitFactions(self)

class Faction(AST_Node):
    def __init__(self, identifier):
        self.identifier: Identifier = identifier

    def accept(self, visitor):
        visitor.visitFaction(self)

class Relations:
    def __init__(self, relation_list):
        self.relation_list: list[Relation] = relation_list

    def accept(self, visitor):
        visitor.visitRelations(self)

class Relation(AST_Node):
    def __init__(self, faction1, faction2, relation):
        self.faction1: str = faction1
        self.faction2: str = faction2
        self.relation: int = relation

    def accept(self, visitor):
        visitor.visitRelation(self)

class Fleets(AST_Node):
    def __init__(self, faction_fleet):
        self.faction_fleet: list[Faction_Fleet] = faction_fleet

    def accept(self, visitor):
        visitor.visitFleets(self)

class Faction_Fleet(AST_Node):
    def __init__(self, faction,flotilla_list):
        self.faction: str = faction
        self.flotilla_list: list[Flotilla] = flotilla_list

class Flotilla(AST_Node):
    def __init__(self, identifier, vessels):
        self.identifier: Identifier = identifier
        self.vessels: list[Vessel] = vessels

    def accept(self, visitor):
        visitor.visitFlotilla(self)

class Vessel(AST_Node):
    def __init__(self, number, vessel_type):
        self.number: int = number
        self.vessel_type: Vessel_type = vessel_type

    def accept(self, visitor):
        visitor.visitVessel(self)

class Vessel_type(AST_Node):
    def __init__(self, type):
        self.type:str = type

    def accept(self, visitor):
        visitor.visitVessel_type(self)


class Map(AST_Node):
    def __init__(self, x,y):
        self.x: int = x
        self.y: int = y

    def accept(self, visitor):
        visitor.visitMap(self)

class Identifier(AST_Node):
    def __init__(self, name):
        self.name: str = name

    def accept(self, visitor):
        visitor.visitIdentifier(self)
