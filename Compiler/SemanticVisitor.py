import sys
import warnings

from AbstractVisitor import Visitor
from NavalWargamingAbstractSyntax import Empty, Identifier, Relation
import config


class SemanticVisitor(Visitor):
    """Visit all nodes
    - Change none node in empty node
    - Checks the declaration of variables
    - Intialize the wargame
    """

    def __init__(self):
        self.faction = set()
        self.faction_multi_decl = set()
        self.relation= {}
        self.navy = {}
        self.flotilla = set()

    def reset(self):
        self.faction = set()

    def InitializeWargame(self):
        pass #todo

    def normalize_countries(self,countries, separator="-"):
        return separator.join(sorted(countries.split(separator)))

    def visit(self, Program):
        self.reset()
        Program.accept(self)

    def visitProgram(self, Program):
        Program.initial_State.accept(self)
        for action in Program.actions:
            action.accept(self)

    def visitInitial_State(self, Initial_State):
        if (Initial_State.factions is None):
            Initial_State.factions = Empty()
        else:
            Initial_State.factions.accept(self)

        if (Initial_State.relations is None):
            Initial_State.relations = Empty()
        else:
            Initial_State.relations.accept(self)

        if (Initial_State.fleets is None):
            Initial_State.fleets = Empty()
        else:
            Initial_State.fleets.accept(self)

        Initial_State.map.accept(self)

    def visitFactions(self, Factions):
        if (Factions.faction_list == []):
            Factions.faction_list = [Empty()]
            warnings.warn("No faction declared")
        else:
            for faction in Factions.faction_list:
                faction.accept(self)

    def visitFaction(self, Faction):
        Faction.identifier.accept(self)
        if Faction.identifier.name in self.faction:
            warnings.warn("Faction " + Faction.identifier.name + " already declared")
        else:
            self.faction.add(Faction.identifier.name)

    def visitRelations(self, Relations):
        if not Relations.relation_list:
            Relations.relation_list = [Empty()]
            warnings.warn("No relation declared")
        else:
            for relation in Relations.relation_list:
                relation.accept(self)
        self.verify_relation_presence(Relations)

    def verify_relation_presence(self,Relations):
        for faction in self.faction:
            for faction2 in self.faction:
                if faction != faction2:
                    if self.normalize_countries(faction+"-"+faction2) not in self.relation:
                        self.relation[self.normalize_countries(faction+"-"+faction2)] = 0
                        Relations.relation_list.append(Relation(Identifier(faction),Identifier(faction2),str(0)))
                        warnings.warn("Relation between "+faction+" and "+faction2+" not declared, set to 0")

    def visitRelation(self, Relation):
        Relation.faction1.accept(self)
        Relation.faction2.accept(self)

        if(Relation.faction1.name == Relation.faction2.name):
            raise ValueError("Faction cannot be in relation with itself ("+Relation.faction1.name+")")
        elif(Relation.faction1.name not in self.faction):
            raise ValueError("Faction "+Relation.faction1.name+" not declared")
        elif(Relation.faction2.name not in self.faction):
            raise ValueError("Faction "+Relation.faction2.name+" not declared")
        elif(self.normalize_countries(Relation.faction1.name+"-"+Relation.faction2.name) in self.relation):
            raise ValueError("Relation between "+Relation.faction1.name+" and "+Relation.faction2.name+" already declared")

        self.relation[self.normalize_countries(Relation.faction1.name+"-"+Relation.faction2.name)] = int(Relation.relation)


    def visitFleets(self, Fleets):
        if (Fleets.faction_fleet == []):
            Fleets.faction_fleet = [Empty()]
            warnings.warn("No fleet declared")
        else:
            for fleet in Fleets.faction_fleet:
                fleet.accept(self)

    def visitFaction_Fleet(self, Faction_Fleet):
        Faction_Fleet.faction.accept(self)

        if Faction_Fleet.faction.name not in self.faction:
            raise ValueError("In faction fleet, Faction " + Faction_Fleet.faction.name + " not declared")
        elif (Faction_Fleet.faction.name in self.navy):
            raise ValueError("Faction Fleet " + Faction_Fleet.faction.name + " already declared")

        self.navy[Faction_Fleet.faction.name] = {}

        if (Faction_Fleet.flotilla_list == []):
            Faction_Fleet.flotilla_list = [Empty()]
            warnings.warn("No flotilla declared")
        else:
            for flotilla in Faction_Fleet.flotilla_list:
                flotilla.accept(self)

    def visitFlotilla(self, Flotilla):
        Flotilla.identifier.accept(self)
        if(Flotilla.identifier.name in self.flotilla):
            raise ValueError("Flotilla " + Flotilla.identifier.name + " already declared")
        self.flotilla.add(Flotilla.identifier.name)

        if (Flotilla.vessels == []):
            raise ValueError("No vessel declared in flotilla " + Flotilla.identifier.name)

        for vessel in Flotilla.vessels:
            vessel.accept(self)

    def visitVessel(self, Vessel):
        # Vessel.number
        Vessel.vessel_type.accept(self)

    def visitVessel_Type(self, Vessel_Type):
        if Vessel_Type.type not in config.vesselTypePossible:
            raise ValueError("Vessel type " + Vessel_Type.type + " not possible")

    def visitMap(self, Map):
        print(Map.x)
        self.Test_MAP_Value(int(Map.x), "Map x")
        self.Test_MAP_Value(int(Map.y), "Map y")

    def Test_MAP_Value(self, mapValue, name):
        if (mapValue > config.MAP_MAX):
            warnings.warn("The value of " + name + " is too high, it will be set to " + str(config.MAP_MAX))
            mapValue = config.MAP_MAX
        elif (mapValue < config.MAP_MIN):
            warnings.warn("The value of " + name + " is too low, it will be set to " + str(config.MAP_MIN))
            mapValue = config.MAP_MIN

    def visitIdentifier(self, Identifier):
        # Identifier.name
        pass
