import attacks as atk



class Hero:
    pucklist = [atk.Moves("Illusory Orb", 15), atk.Moves("Waning Rift", 30), atk.Moves("Phase Shift", 0), atk.Moves("Dream Coil", 15)]
    tinkerlist = [atk.Moves("Laser", 30), atk.Moves("Heat-Seeking Missile", 40), atk.Moves("March of the Machines", 10), atk.Moves("Rearm", 0)]

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

    def Getpuck_attack1(self):
        return self.pucklist[0]

    def Getpuck_attack2(self):
        return self.pucklist[1]

    def Getpuck_attack3(self):
        return self.pucklist[2]

    def Getpuck_attack4(self):
        return self.pucklist[3]

    def Gettinker_attack1(self):
        return self.tinkerlist[0]

    def Gettinker_attack2(self):
        return self.tinkerlist[1]

    def Gettinker_attack3(self):
        return self.tinkerlist[2]

    def Gettinker_attack4(self):
        return self.tinkerlist[3]

    def GetallPuckattacks(self):
        return self.pucklist

    def Getalltinkerattacks(self):
        return self.tinkerlist















