import matplotlib.pyplot as plt

class NavalWargamingMap():
    """
    This class is the map of the simulation.
    """

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.grid = [[' ' for _ in range(x)] for _ in range(y)]

    def showMap(self,fleets,factions):
        color_legend = [['C{}'.format(i),fact] for i,fact in enumerate(factions)]
        fig, ax = plt.subplots()

        ax.set_facecolor('xkcd:sky blue')

        for flotilla in fleets:
            x = flotilla.x
            y = flotilla.y
            index = factions.index(flotilla.faction)
            color = 'C{}'.format(index)
            ax.scatter(x, y, marker='x', s=200, linewidth=3, color=color)
            ax.annotate(flotilla.name, xy=(x + 0.2, y - 0.2), fontsize=14)

        ax.set_xlim([-0.5, self.x - 0.5])
        ax.set_ylim([-0.5, self.y - 0.5])

        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

        handles = [plt.Line2D([], [], color=color, label=faction) for color, faction in color_legend]
        ax.legend(handles=handles)

        plt.show()


