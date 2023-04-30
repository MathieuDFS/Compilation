import sys
from AbstractVisitor import Visitor
from NavalWargamingAbstractSyntax import Empty

class EmptyVisitor(Visitor):
    """Visit all nodes and change none node in empty node
    Avoir: AttributeError: 'NoneType' object has no attribute 'accept'
    """

    def visit(self, Program):
        Program.accept(self)

    def visitProgram(self, Program):
        Program.initial_State.accept(self)
        for action in Program.actions:
            action.accept(self)

    def visitInitial_State(self, Initial_State):
        if(Initial_State.factions is None):
            Initial_State.factions = Empty()
        else:
            Initial_State.factions.accept(self)

        if(Initial_State.relations is None):
            Initial_State.relations = Empty()
        else:
            Initial_State.relations.accept(self)

        if(Initial_State.fleets is None):
            Initial_State.fleets = Empty()
        else:
            Initial_State.fleets.accept(self)

        Initial_State.map.accept(self)

    def visitFactions(self, Factions):
        if (Factions.faction_list == []):
            Factions.faction_list = [Empty()]
        else:
            for faction in Factions.faction_list:
                faction.accept(self)

    def visitFaction(self, Faction):
        Faction.identifier.accept(self)

    def visitRelations(self, Relations):
        if(Relations.relation_list == []):
            Relations.relation_list = [Empty()]
        else :
            for relation in Relations.relation_list:
                relation.accept(self)

    def visitRelation(self, Relation):
        Relation.faction1.accept(self)
        Relation.faction2.accept(self)
        # Relation.relation

    def visitFleets(self, Fleets):
        if (Fleets.faction_fleet == []):
            Fleets.faction_fleet = [Empty()]
        else:
            for fleet in Fleets.faction_fleet:
                fleet.accept(self)

    def visitFaction_Fleet(self, Faction_Fleet):
        Faction_Fleet.faction.accept(self)

        if(Faction_Fleet.flotilla_list == []):
            Faction_Fleet.flotilla_list = [Empty()]
        else:
            for flotilla in Faction_Fleet.flotilla_list:
                flotilla.accept(self)

    def visitFlotilla(self, Flotilla):
        Flotilla.identifier.accept(self)
        for vessel in Flotilla.vessels:
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