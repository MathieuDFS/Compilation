from Compiler.AbstractVisitor import Visitor


class PrettyPrinter(Visitor):
    """Visit all nodes
    and Rewrites the code with the basic formatting
    """

    def __int__(self):
        self.filename = None
        self.file = None

    def visit(self, Program, Filename):
        self.filename: str = Filename
        Program.accept(self)

    def visitProgram(self, Program):
        self.file = open(self.filename+".pp.nwg", "w")
        self.file.write("#"+self.filename+" Pretty print\n")
        Program.initial_State.accept(self)
        self.file.close()

    def visitInitial_State(self, Initial_State):
        Initial_State.factions.accept(self)
        Initial_State.relations.accept(self)
        Initial_State.fleets.accept(self)
        Initial_State.map.accept(self)

    def visitFactions(self, Factions):
        self.file.write("\n")
        self.file.write("Factions:\n")
        for faction in Factions.faction_list:
            faction.accept(self)

    def visitFaction(self, Faction):
        self.file.write("\t-")
        Faction.identifier.accept(self)
        self.file.write("\n")

    def visitRelations(self, Relations):
        self.file.write("\n")
        self.file.write("Relations:\n")
        for relation in Relations.relation_list:
            relation.accept(self)

    def visitRelation(self, Relation):
        self.file.write("\t-")
        Relation.faction1.accept(self)
        self.file.write("-")
        Relation.faction2.accept(self)
        self.file.write(": ")
        self.file.write(Relation.relation+"\n")

    def visitFleets(self, Fleets):
        self.file.write("\n")
        self.file.write("Fleets:\n")
        for fleet in Fleets.faction_fleet:
            fleet.accept(self)

    def visitFaction_Fleet(self, Faction_Fleet):
        self.file.write("\t-")
        Faction_Fleet.faction.accept(self)
        self.file.write(" fleet:\n")
        for flotilla in Faction_Fleet.flotilla_list:
            flotilla.accept(self)

    def visitFlotilla(self, Flotilla):
        self.file.write("\t\t-")
        Flotilla.identifier.accept(self)
        self.file.write(":\n")
        for vessel in Flotilla.vessels:
            vessel.accept(self)
        self.file.write("\n")

    def visitVessel(self, Vessel):
        self.file.write("\t\t\t")
        self.file.write(Vessel.number + " ")
        Vessel.vessel_type.accept(self)

    def visitVessel_Type(self, Vessel_Type):
        self.file.write(Vessel_Type.type + "\n")


    def visitMap(self, Map):
        self.file.write("Map:\n")
        self.file.write("\t")
        self.file.write(str(Map.x) + "*" + str(Map.y) + "\n")

    def visitIdentifier(self, Identifier):
        self.file.write(Identifier.name)