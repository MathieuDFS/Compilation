import sys
from AbstractVisitor import Visitor


class PrettyPrinter(Visitor):
    def __int__(self,output):
        self.output = output
        self.file = None

    def visit(self, Program):
        Program.accept(self)

    def visitProgram(self, Program):
        self.file = open("test.nwg", "w")
        self.file.write("#Program Pretty print\n")
        Program.initial_State.accept(self)
        for action in Program.actions:
            action.accept(self)
        self.file.close()

    def visitInitial_State(self, Initial_State):
        Initial_State.factions.accept(self)
        Initial_State.relations.accept(self)
        Initial_State.fleets.accept(self)
        Initial_State.map.accept(self)

    def visitFactions(self, Factions):
        for faction in Factions.faction_list:
            faction.accept(self)

    def visitFaction(self, Faction):
        Faction.identifier.accept(self)

    def visitRelations(self, Relations):
        for relation in Relations.relation_list:
            relation.accept(self)

    def visitRelation(self, Relation):
        Relation.faction1.accept(self)
        Relation.faction2.accept(self)
        # Relation.relation

    def visitFleets(self, Fleets):
        for fleet in Fleets.faction_fleet:
            fleet.accept(self)

    def visitFaction_Fleet(self, Faction_Fleet):
        Faction_Fleet.identifier.accept(self)
        for flotilla in Faction_Fleet.flotilla_list:
            flotilla.accept(self)

    def visitFlotilla(self, Flotilla):
        Flotilla.identifier.accept(self)
        for vessel in Flotilla.vessel_list:
            vessel.accept(self)

    def visitVessel(self, Vessel):
        # Vessel.number
        Vessel.vessel_type.accept(self)

    def visitVessel_Type(self, Vessel_Type):
        # Vessel_Type.type
        pass

    def visitMap(self, Map):
        # Map.x
        # Map.y
        pass

    def visitIdentifier(self, Identifier):
        # Identifier.name
        pass