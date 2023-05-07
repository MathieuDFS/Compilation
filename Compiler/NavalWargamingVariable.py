import warnings


class NavalWargamingVariable():
    """A class that contains all the variables for the naval wargame, and the tests to initialize its variables"""
    def __init__(self):
        #Useful for initalization
        self.relationDeclMarker = {}

        #Useful for simulation
        self.faction = []
        self.relation= {}
        self.navy = {}
        self.map = ()

    def normalize_countries(self,countries, separator="-"):
        return separator.join(sorted(countries.split(separator)))

    def __str__(self):
        return ("Factions: " + str(self.faction) + "\nRelations: " + str(self.relation) + "\nNavy: " + str(self.navy)+ "\nMap: " + str(self.map))

    #######################
    # Faction declaration
    #######################
    def addFaction(self, faction):
        if faction in self.faction:
            warnings.warn("Faction " + faction.identifier.name + " already declared")
        else:
            self.faction.append(faction)
            return True

    #######################
    # Relation declaration
    #######################

    def createRelationDataBase(self):
        for index,faction1 in enumerate(self.faction):
            for faction2 in self.faction[index+1:]:
                self.relation[self.normalize_countries(faction1+"-"+faction2)] = 0

        self.relationDeclMarker = {key: False for key in self.relation}

    def addRelation(self,Relation):
        if(Relation.faction1.name == Relation.faction2.name):
            raise ValueError("Faction cannot be in relation with itself ("+Relation.faction1.name+")")
        elif(Relation.faction1.name not in self.faction):
            raise ValueError("Faction "+Relation.faction1.name+" not declared")
        elif(Relation.faction2.name not in self.faction):
            raise ValueError("Faction "+Relation.faction2.name+" not declared")
        elif(self.relationDeclMarker[self.normalize_countries(Relation.faction1.name+"-"+Relation.faction2.name)]):
            raise ValueError("Relation between "+Relation.faction1.name+" and "+Relation.faction2.name+" already declared")
        else:
            self.relation[self.normalize_countries(Relation.faction1.name+"-"+Relation.faction2.name)] = int(Relation.relation)
            self.relationDeclMarker[self.normalize_countries(Relation.faction1.name+"-"+Relation.faction2.name)] = True

    def testRelationDeclaration(self):
        for key in self.relationDeclMarker:
            if not self.relationDeclMarker[key]:
                warnings.warn("Relation "+key+" not declared, set to 0")

    #######################
    # Fleet declaration
    #######################

    def addFactionFleet(self,Faction_Fleet):
        if Faction_Fleet.faction.name not in self.faction:
            raise ValueError("In faction fleet, Faction "+Faction_Fleet.faction.name+" not declared")
        elif Faction_Fleet.faction.name in self.navy:
            raise ValueError("Faction fleet "+Faction_Fleet.faction.name+" already declared")
        else:
            self.navy[Faction_Fleet.faction.name] = {}

    def addFlotilla(self,Flotilla,faction,vessels):
        if faction.name not in self.faction:
            raise ValueError("In Flotilla, Faction " + faction.name + " not declared")
        elif faction.name not in self.navy:
            raise ValueError("In Flotilla, Faction "+faction.name+" does not have faction fleet")
        elif Flotilla.identifier.name in self.navy[faction.name]:
            raise ValueError("Flotilla "+Flotilla.identifier.name+" already declared")
        else:
            self.navy[faction.name][Flotilla.identifier.name] = {}
            for vessel in vessels:
                self.navy[faction.name][Flotilla.identifier.name][vessel.vessel_type.type] = int(vessel.number)

    def testFactionWhithoutFleet(self):
        for faction in self.faction:
            if faction not in self.navy:
                warnings.warn("Faction "+faction+" does not have any fleet")

    #######################
    # Map declaration
    #######################

    def setMap(self,x,y):
        self.map = (int(x),int(y))
