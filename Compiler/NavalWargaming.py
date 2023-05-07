from NavalWargamingVariable import NavalWargamingVariable

class NavalWargaming():
    def __init__(self, variable :  NavalWargamingVariable):
        if not isinstance(variable, NavalWargamingVariable):
            raise TypeError("variable must be of type NavalWargamingVariable")
        self.variable = variable
