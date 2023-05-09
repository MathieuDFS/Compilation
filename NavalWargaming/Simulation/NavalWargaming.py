import random as rd

from Simulation.NavalWargamingFlotilla import NavalWargamingFlotilla
from Simulation.NavalWargamingMap import NavalWargamingMap
from Simulation.NavalWargamingVariable import NavalWargamingVariable


class NavalWargaming():
    """
    This class is the main class of the simulation.
    """
    def __init__(self):
        self.map = None
        self.factions = []
        self.relations = None
        self.fleets = []


    def initialization(self,initialization_variable):
        """
        This method initialize the simulation with the variable given by the compiler.
        """
        if not isinstance(initialization_variable, NavalWargamingVariable):
            raise TypeError("variable must be of type NavalWargamingVariable")

        #Faction definition
        self.factions = initialization_variable.faction

        #Relation definition
        self.relations = initialization_variable.relation

        #Map definition
        self.map = NavalWargamingMap(initialization_variable.map[0], initialization_variable.map[1])

        #Fleet definition
        for faction in initialization_variable.navy:
            for flotilla_name in initialization_variable.navy[faction]:
                #coordonnee random
                x=rd.randint(0, self.map.x)
                y=rd.randint(0,self.map.y)

                nwgFlotilla = NavalWargamingFlotilla(faction, flotilla_name, initialization_variable.navy[faction][flotilla_name],x,y)
                self.fleets.append(nwgFlotilla)


    def run(self):
        print("The simulation part has not been implemented yet.")
        print("The simulation will cover the rising tension between ", end="")
        for k in range(len(self.factions)):
            print(self.factions[k], end="")
            if k < len(self.factions)-2:
                print(", ", end="")
            elif k == len(self.factions)-2:
                print(" and ", end="")
            else:
                print(".")

        print("Their initial relation are ", end="")
        for index,relation in enumerate(self.relations):
            if index < len(self.relations)-2:
                print(relation, self.relations[relation], end=", ")
            elif index == len(self.relations)-2:
                print(relation, self.relations[relation], end=" and ")
            else:
                print(relation, self.relations[relation], end=".")
        print("(between -100 and 100).")

        print("There are "+str(len(self.fleets))+" fleets in presence.", end=" ")
        for index,fleet in enumerate(self.fleets):
            if index < len(self.fleets)-2:
                print(fleet.name, "from", fleet.faction, end=", ")
            elif index == len(self.fleets)-2:
                print(fleet.name, "from", fleet.faction, end=" and ")
            else:
                print(fleet.name, "from", fleet.faction, end=".\n")


        print("The simulation will cover ", self.map.x, "x", self.map.y, "km.")
        print("Here is the map:")
        self.map.showMap(self.fleets, self.factions)

