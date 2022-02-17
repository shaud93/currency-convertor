


class Convert:
    
    def ___init__(self, name):
        self.name = name

    def CheckType(self, var):
        x = isinstance(var, (int, float))
        return x