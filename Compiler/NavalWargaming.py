from NavalWargamingVariable import NavalWargamingVariable
from NavalWargamingMap import NavalWargamingMap
from NavalWargamingFlotilla import NavalWargamingFlotilla
import random as rd

class NavalWargaming():
    def __init__(self):
        self.map = None
        self.factions = []
        self.relations = None
        self.fleets = []


    def initialization(self,initialization_variable):
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

        self.map.showMap(self.fleets,self.factions)

