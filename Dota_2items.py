class Items:

    def __init__(self, name , gold):
        self.name = name
        self.gold = gold

    def Getitemname(self):
        return self.name

    def Getitemgold(self):
        return self.gold

    def SetitemWorth(self, value):
        self.gold = value



