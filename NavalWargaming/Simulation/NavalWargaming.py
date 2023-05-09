import random as rd

from NavalWargaming.Simulation.NavalWargamingFlotilla import NavalWargamingFlotilla
from NavalWargaming.Simulation.NavalWargamingMap import NavalWargamingMap
from NavalWargaming.Simulation.NavalWargamingVariable import NavalWargamingVariable


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
        self.map.showMap(self.fleets,self.factions)
        print("The simulation part has not been implemented yet.")


