
class NavalWargamingFlotilla():
    """
    This class is the flotilla class of the simulation.
    """
    def __init__(self,faction,name,vessels,x,y):
        self.faction = faction
        self.name = name
        self.vessels = vessels
        self.x = x
        self.y = y

    def __str__(self):
        return ("Faction: " + str(self.faction) + "\nName: " + str(self.name) + "\nVessels: " + str(self.vessels)+ "\nPosition: " + str(self.x) + "," + str(self.y))


