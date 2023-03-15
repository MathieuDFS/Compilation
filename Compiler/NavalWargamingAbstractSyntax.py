
class AST_Node():
    """Abstract class for AST nodes"""
    pass



class Program(AST_Node):
    def __init__(self,initial_State, actions):
        self.initial_State: Initial_State = initial_State
        self.actions: list(Action) = actions


class Initial_State(AST_Node):
    def __init__(self, terrain, factions, relations, fleets):
        self.factions: list(Factions) = factions
        self.relations: list(Relations) = relations
        self.fleets: list(Fleets) = fleets
        self.terrain : Terrain = terrain

class Action(AST_Node):
    pass #todo

class Factions(AST_Node):
    def __init__(self, faction_list):
        self.faction_list: list(Faction) = faction_list
class Faction(AST_Node):
    def __init__(self, name):
        self.name: str = name

class Relations:
    def __init__(self, relation_list):
        self.relation_list: list(Relation) = relation_list
class Relation(AST_Node):
    def __init__(self, faction1, faction2, relation):
        self.faction1: str = faction1
        self.faction2: str = faction2
        self.relation: int = relation

class Fleets(AST_Node):
    def __init__(self, faction_fleet):
        self.faction_fleet: list(Faction_Fleet) = faction_fleet

class Faction_Fleet(AST_Node):
    def __init__(self, faction,flotilla_list):
        self.faction: str = faction
        self.flotilla_list: list(Flotilla) = flotilla_list

class Flotilla(AST_Node):
    def __init__(self, name, vessels):
        self.name: str = name
        self.vessels: list(Vessel) = vessels

class Vessel(AST_Node):
    def __init__(self, number, vessel_type):
        self.number: int = number
        self.vessel_type: Vessel_type = vessel_type

class Vessel_type(AST_Node):
    def __init__(self, type):
        self.type:str = type

class Terrain(AST_Node):
    def __init__(self, x,y):
        self.x: int = x
        self.y: int = y
