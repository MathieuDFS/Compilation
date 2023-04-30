from abc import ABCMeta, abstractmethod
import NavalWargamingAbstractSyntax

class Visitor(metaclass=ABCMeta):

    @abstractmethod
    def visit(self, Program):
        """Start to visit"""
        pass

    @abstractmethod
    def visitProgram(self, Program):
        pass

    @abstractmethod
    def visitInitial_State(self, Initial_State):
        pass

    @abstractmethod
    def visitFactions(self, Factions):
        pass

    @abstractmethod
    def visitFaction(self, Faction):
        pass

    @abstractmethod
    def visitRelations(self, Relations):
        pass

    @abstractmethod
    def visitRelation(self, Relation):
        pass

    @abstractmethod
    def visitFleets(self, Fleets):
        pass

    @abstractmethod
    def visitFaction_Fleet(self, Faction_Fleet):
        pass

    @abstractmethod
    def visitFlotilla(self, Flotilla):
        pass

    @abstractmethod
    def visitVessel(self, Vessel):
        pass

    @abstractmethod
    def visitVessel_Type(self, Vessel_Type):
        pass

    @abstractmethod
    def visitMap(self, Map):
        pass

    @abstractmethod
    def visitIdentifier(self, Identifier):
        pass