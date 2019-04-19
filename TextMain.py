import time
#import Dota_2items as item
import Hero as hero


import random


puck = hero.Hero("puck", 100)
tinker = hero.Hero("tinker", 100)

heroes = []


heroes.append(puck)
heroes.append(tinker)

#getmoves = atk.Moves.GetallPuckattacks()




#leaving auto attacks here because i would have to change the code to reflect it using the new list in the other class
puck_auto = hero.atk.Moves("basic attack", 5)

tinker_auto = hero.atk.Moves("basic attack", 7)



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


# Making this a function so i can use it in the future for a different lane,hero ,etc...

def Lanegame():

    print("The game starts and gavin is facing a " + tinker.Getname() +" mid")
    time.sleep(2)
    print("He goes in with tangoes, magic stick, and branches")
    time.sleep(2)


    while True:
        if (puck.Gethp() > 0):
            print("Choose what you want to:")
            time.sleep(2)
            print("1.try to farm the wave")
            time.sleep(.5)
            print("2.poke the " + tinker.Getname() + " down with auto attacks ")
            time.sleep(.5)
            print("3.use a move")
            time.sleep(2)
            print("Gavin....")


        pickoption = input(":")
        if pickoption == "1":
            print(" see's an opportunity to get farm and.....")
            random_farm = random.randint(1, 2)
            if random_farm == 1:
                time.sleep(1)
                print("get's some of the wave! he compliments himself in his mind knowing he at least got some farm")
            if random_farm == 2:
                time.sleep(1)
                print("got unlucky because " + tinker.Getname() + " happened get farm at the same time and hit you with his "+ laser.Getname() +" making you miss! you take damage and get no farm! ")
                lossHp = puck.Sethp(puck.Gethp() - laser.GetDamage())
                print("you took " + (str(laser.GetDamage())) + " Damage and now have " + (str(puck.Sethp(lossHp))) + "Hp")
        if pickoption == "2":
            print("decides that he can try to poke him down with auto attacks and...")
            random_auto = random.randint(1,2)

            random_timeshit = random.randint(1,4)

            totalhit_1 = random_timeshit * puck_auto.GetDamage()

            totalhit_2 = random_timeshit * tinker_auto.GetDamage()

            lossAutohp_1 = tinker.Sethp(tinker.Gethp() - totalhit_1)
            lossAutohp_2 = puck.Sethp(puck.Gethp() - totalhit_2)
            if random_auto == 1:
                time.sleep(1)
                print("and catches him off guard and was able to hit him " + (str(random_timeshit)) + " times for " + (str(totalhit_1)) + " and now has " + (str(lossAutohp_1)) + " hp")
            if random_auto == 2:
                time.sleep(1)
                print("he fails to notice that the " + tinker.Getname() + " was uphill and with his")
                print("horrible luck he misses every auto but tinker was able to hit him " + (str(random_timeshit)))
                print(" times for " + (str(totalhit_2)) + " hp and now have " + (str(lossAutohp_2)) + " Hp")
        if pickoption == "3":
            print("in his mind thinks on what move would be correct")
            for item in puck.pucklist:
                print(item.Getname())




            #for x in (len(puckmoves)):
             #   print(vars(puckmoves(x)))
              #  break
            choose_move_input = input(": ")




        else:
            time.sleep(1)
            print("While you were trying to show off how good you are as " + puck.Getname() + " you failed to notice that ")
            print(tinker.Getname() + " already has you locked down and kills you!")
            break









Lanegame()

















