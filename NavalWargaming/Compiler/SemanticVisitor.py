import warnings

from Compiler.AbstractVisitor import Visitor
from Compiler.NavalWargamingAbstractSyntax import Empty
from Simulation import config
from Simulation.NavalWargaming import NavalWargaming
from Simulation.NavalWargamingVariable import NavalWargamingVariable


class SemanticVisitor(Visitor):
    """Visit all nodes
    - Change none node in empty node
    - Checks the declaration of variables
    - Create the initialization variables for the simulation
    """

    def __init__(self):
        self.nwgVariable =None
        self.nwg = None

    def InitializeWargame(self):
        return NavalWargaming().initialization(self.nwgVariable)

    def visit(self, Program):
        self.nwgVariable = NavalWargamingVariable()
        Program.accept(self)

    def visitProgram(self, Program):
        Program.initial_State.accept(self)

    def visitInitial_State(self, Initial_State):
        if (Initial_State.factions is None):
            Initial_State.factions = Empty()
            warnings.warn("No faction declared")
        else:
            Initial_State.factions.accept(self)

        self.nwgVariable.createRelationDataBase()
        if (Initial_State.relations is None):
            Initial_State.relations = Empty()
            warnings.warn("No relation declared")
        else:
            Initial_State.relations.accept(self)
        self.nwgVariable.testRelationDeclaration()

        if (Initial_State.fleets is None):
            Initial_State.fleets = Empty()
            warnings.warn("No fleet declared")
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
        self.nwgVariable.addFaction(Faction.identifier.name)

    def visitRelations(self, Relations):
        if not Relations.relation_list:
            Relations.relation_list = [Empty()]
            warnings.warn("No relation declared")
        else:
            for relation in Relations.relation_list:
                relation.accept(self)

    def visitRelation(self, Relation):
        Relation.faction1.accept(self)
        Relation.faction2.accept(self)
        self.nwgVariable.addRelation(Relation)

    def visitFleets(self, Fleets):
        if (Fleets.faction_fleet == []):
            Fleets.faction_fleet = [Empty()]
            warnings.warn("No fleet declared")
        else:
            for fleet in Fleets.faction_fleet:
                fleet.accept(self)
        self.nwgVariable.testFactionWhithoutFleet()

    def visitFaction_Fleet(self, Faction_Fleet):
        self.nwgVariable.addFactionFleet(Faction_Fleet)
        Faction_Fleet.faction.accept(self)

        if (Faction_Fleet.flotilla_list == []):
            Faction_Fleet.flotilla_list = [Empty()]
            warnings.warn("No flotilla declared for faction fleet " + Faction_Fleet.faction.name + "")
        else:
            for flotilla in Faction_Fleet.flotilla_list:
                flotilla.acceptAndTransmitFaction(self,Faction_Fleet.faction)

    def visitFlotilla(self, Flotilla,faction=None):
        if faction is None:
            raise ValueError("Faction not transmitted")

        Flotilla.identifier.accept(self)

        for vessel in Flotilla.vessels:
            vessel.accept(self)

        self.nwgVariable.addFlotilla(Flotilla,faction,Flotilla.vessels)

    def visitVessel(self, Vessel):
        Vessel.vessel_type.accept(self)

    def visitVessel_Type(self, Vessel_Type):
        if Vessel_Type.type not in config.vesselTypePossible:
            raise ValueError("Vessel type " + Vessel_Type.type + " not possible")

    def visitMap(self, Map):
        Map.x = self.Test_MAP_Value(int(Map.x), "Map x")
        Map.y = self.Test_MAP_Value(int(Map.y), "Map y")
        self.nwgVariable.setMap(Map.x,Map.y)

    def Test_MAP_Value(self, mapValue, name):
        if (mapValue > config.MAP_MAX):
            warnings.warn("The value of " + name + " is too high, it will be set to " + str(config.MAP_MAX))
            mapValue = config.MAP_MAX
        elif (mapValue < config.MAP_MIN):
            warnings.warn("The value of " + name + " is too low, it will be set to " + str(config.MAP_MIN))
            mapValue = config.MAP_MIN
        return mapValue

    def visitIdentifier(self, Identifier):
        pass
