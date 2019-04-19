class Moves():


    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


    def Getname(self):
        return self.name

    def GetDamage(self):
        return self.damage

    def SetDamage(self, value):
        self.damage = value
        return self.SetDamage()


