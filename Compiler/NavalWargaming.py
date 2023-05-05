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
        self.flotilla = set()

    def normalize_countries(self,countries, separator="-"):
        return separator.join(sorted(countries.split(separator)))

    def __str__(self):
        return ("Factions: " + str(self.faction) + "\nRelations: " + str(self.relation))

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




class NavalWargaming():
    def __init__(self, variable :  NavalWargamingVariable):
        if not isinstance(variable, NavalWargamingVariable):
            raise TypeError("variable must be of type NavalWargamingVariable")
        self.variable = variable
