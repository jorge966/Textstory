import time
#import Dota_2items as item
import Hero as hero
import attacks as atk
import random


puck = hero.Hero("puck", 100)
tinker = hero.Hero("tinker", 100)


puck_auto = atk.Moves("basic attack", 5)
Illusory_orb = atk.Moves("Illusory Orb", 15)
Phase_Shift = atk.Moves("Phase Shift", 0)
Waning_Rift = atk.Moves("Waning Rift", 30)
Dream_Coil = atk.Moves("Dream Coil", 20)
tinker_auto = atk.Moves("basic attack", 7)
laser = atk.Moves("Laser", 30)
Heat_Seeking_Missile = atk.Moves("Heat-Seeking Missile", 40)
March_of_the_Machines = atk.Moves("March of the Machines", 10)
Rearm = atk.Moves("Rearm", 0)





puckmoves = []

puckmoves.append(puck_auto)
puckmoves.append(Illusory_orb)
puckmoves.append(Phase_Shift)
puckmoves.append(Waning_Rift)
puckmoves.append(Dream_Coil)




tinkermoves = []

tinkermoves.append(tinker_auto)
tinkermoves.append(laser)
tinkermoves.append(Heat_Seeking_Missile)
tinkermoves.append(March_of_the_Machines)
tinkermoves.append(Rearm)






startingitemsDict = {
    "tango's": ["Tango's", 90],
    "magic wand": ["magic wand", 120],
    "branch": ["branch", 50],
    "healing salve": ["healing salve", 110],
    "clarity": ["Clarity", 50],
    "bottle": ["Bottle", 650]
}



def Intro():

        print("########################################################")
        print("Welcome to a Day in life of Gavin")
        print("")
        time.sleep(2)
        print("in this Text adventure we will see how the god himself plays a game Dota 2")
        print("")
        time.sleep(3)
        print("this story begins with gavin accepting a game and getting into the character select")
        print("")
        time.sleep(2)
        print("Gavin sees that the team needs a valuable support that will make this an easy game.....")
        print("")
        time.sleep(2)
        print("So of course he picks Puck because he believe's that Puck mid will be better")
        print("")
        time.sleep(2)
        print('in the background he hears Ed saying angrily "Why did you pick puck when you needed a support?"')
        time.sleep(2)
        print("")
        print("Gavin says with a certain arrogance that he plays an insane puck (in his mmr bracket) and can easily carry")
        time.sleep(2)
#def Earlygame():
 #   while(True):
  #      print("The game starts and gavin is seeing what items to buy")
   #     print("he decides to open a guide to see what other people pick on puck early game")

def MidLanegame():

    print("The game starts and gavin is facing a tinker mid")
    time.sleep(2)
    print("He goes in with tangoes,magic stick, and branches")
    time.sleep(2)
    print("Choose what you want to:")
    time.sleep(2)
    print("1.try to farm the wave")
    time.sleep(.5)
    print("2.poke the tinker down with auto attacks ")
    time.sleep(.5)
    print("3.use a move")
    time.sleep(2)
    print("Gavin....")
    if (puck.Gethp() > 0):
        while True:
            pickoption = input(":")
            if pickoption == "1":
                print(" see's an opportunity to get farm and.....")
                random_input = random.randint(1, 2)
                if random_input == 1:
                    print("get's some of the wave! he compliments himself in his mind knowing he at least got some farm")
                if random_input == 2:
                    print("got unlucky because tinker happened to go get farm at the same time and hit you with his laser making you miss! you take damage and get no farm! ")
                    lossHp = puck.Sethp(puck.Gethp() - laser.GetDamage())
                    print("you took" + (str(laser.GetDamage())) + " Damage and now have " + (str(puck.Sethp(lossHp))) + "Hp")
            else:
                print("You did nothing and died")
                break








MidLanegame()

















