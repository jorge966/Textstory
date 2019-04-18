class Hero:

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


    def Getname(self):
        return self.name

    def Gethp(self):
        return self.hp

    def Setname(self, value):
        self.name = value
        return self.name

    def Sethp(self, value):
        self.hp = value
        if value < 0:
            self.hp = 0
        return self.hp












