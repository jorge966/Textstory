import time
#import Dota_2items as item
import Hero as hero


import random

# just two heroes for right now to start
puck = hero.Hero("puck", 100)
tinker = hero.Hero("tinker", 100)

heroes = []


heroes.append(puck)
heroes.append(tinker)






#leaving auto attacks here because i would have to change the code to reflect it using the new list in the other class
puck_auto = hero.atk.Moves("basic attack", 5)

tinker_auto = hero.atk.Moves("basic attack", 7)


#not being used
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


# Making this a function so i can use it in the future for a different lane,hero ,etc...

def Lanegame():

    print("The game starts and gavin is facing a " + tinker.Getname() +" mid")
    print(" ")
    time.sleep(2)
    print("He goes in with tangoes, magic stick, and branches")
    print((" "))
    time.sleep(2)


    while True:
        if (puck.Gethp() > 0):
            print("###############################################")
            print("Choose what you want to:")
            time.sleep(2)
            print("1.try to farm the wave")
            time.sleep(.5)
            print("2.poke the " + tinker.Getname() + " down with auto attacks ")
            time.sleep(.5)
            print("3.use a move")
            time.sleep(2)
            print("Gavin....")


            pickoption = input(": ")
            if pickoption == "1":
                print(" see's an opportunity to get farm and.....")
                random_farm = random.randint(1, 2)
                if random_farm == 1:
                    time.sleep(1)
                    print("get's some of the wave! he compliments himself in his mind knowing he at least got some farm")

                if random_farm == 2:
                    time.sleep(1)
                    print("got unlucky because " + tinker.Getname() + " happened get farm at the same time and hit you with his "+ tinker.Gettinker_attack1().Getname() +" making you miss! you take damage and get no farm! ")
                    lossHp = puck.Sethp(puck.Gethp() - tinker.Gettinker_attack1().GetDamage())
                    print("you took " + (str(tinker.Gettinker_attack1().GetDamage())) + " Damage and now have " + (str(puck.Sethp(lossHp))) + "Hp")

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
                print("in his mind thinks on what move would be correct:")

                #tempIndexes = {}
                for item in puck.pucklist:
                    print((str(puck.pucklist.index(item))) + " " + item.Getname())



                    # keeping this to just see a different alt to print index if i cant use the .index
                    # was using because i was an idiot and had the puck list not an actual list was using {} instead of []
                    #tempIndexes[i] = item.Getname()
                    #i += 1
                #for key, value in enumerate(tempIndexes.items()):
                    #print("{}. {}".format(value[0], value[1]))

                move_pick = input(": ")
                if move_pick == "0":
                    #made it print out again to make it seem like you dont have to do anything else but in fact have to press 2 or q to q back to safety
                    print("you see that you are very pushed out and are about to get ganked so you " + puck.Getpuck_attack1().Getname() + " away to your turret.......")
                    print("Choose what you want to:")
                    time.sleep(2)
                    print("1.try to farm the wave")
                    time.sleep(.5)
                    print("2.poke the " + tinker.Getname() + " down with auto attacks ")
                    time.sleep(.5)
                    print("3.use a move")
                    time.sleep(2)
                    print("Gavin....")
                    forgot_q = input(": ")
                    if forgot_q == "q" or "2" or "Q":
                        print("of course before you do your next move you remember that you still have to press Q again to teleport back to the tower safely")
                    else:
                        print("you completely forget that you still have to Q AGAIN to get back to teleport back to safety and take heavy damage")
                        randomdamage = random.randint(30, 40)
                        puck.Sethp(puck.Gethp() - randomdamage)
                        print("you now have " + (str(puck.Gethp())) + " Hp")
                if move_pick == "1":
                    print("you get very close to the tinker hoping to catch him with your waning rift and... ")
                    time.sleep(2)
                    randomroll = random.randint(1,2)
                    if randomroll == 1:
                        print("with great success you hit him with your " + puck.Getpuck_attack2().Getname() + " and damage and silence him!")
                        tinker.Sethp(tinker.Gethp() - puck.Getpuck_attack2().GetDamage())
                        print("and with that tinker now has " + (str(tinker.Gethp())) + " Hp")
                    if randomroll == 2:
                        print("with horrible aim you whiff your waning rift and tinker takes advantage and hits you with his " + tinker.Gettinker_attack2().Getname())
                        puck.Sethp(puck.Gethp() - tinker.Gettinker_attack2().GetDamage())
                        print(" you now have " + (str(puck.Gethp())) + " Hp")
                if move_pick == "2":
                    print(" while not paying attention you notice that tinker had a high ground ward and used " + tinker.Gettinker_attack2().Getname() + " to track you")
                    print(" you believe that you can perfectly time it so you can evade the attack and...")
                    time.sleep(2)
                    random_dodge = random.randint(1, 2)
                    if random_dodge == 1:
                        print(" with great skills or just plain luck you dodge the attack and get off scotch free ")
                        time.sleep(2)
                    if random_dodge == 2:
                        print(" and with horrible reactions you completely misread the timing and get hit with his attack before you blink out")
                        puck.Sethp(puck.Gethp() - tinker.Gettinker_attack2().GetDamage())
                        print(" you now have " + (str(puck.Gethp())) + " Hp")
                        time.sleep(2)
                if move_pick == "3":
                    print("you notice that two people are tp'ing mid to help and you notice tinker right next to the turret")
                    time.sleep(2)
                    print("you also notice your tema also tp'ing and getting a 3 man ulti on this fight will win you that fight")
                    time.sleep(2)
                    print("so you Q in to get closer and...")
                    time.sleep(2)
                    random_ulti = random.randint(1,2)
                    if random_ulti == 1:
                        print("With exceptional timing you are able to get the three in your ulti and your teammates")
                        tinker.Sethp(tinker.Gethp() - puck.Getpuck_attack4().GetDamage())
                        random_damage = random.randint(20, 30)
                        tinker.Sethp(tinker.Gethp() - random_damage)
                        if tinker.Gethp() > 0:
                            print("were able to kil the enemies that tp'ed and damage the tinker for quite a bit")
                            time.sleep(2)
                            print("tinker now has " + (str(tinker.Gethp())) + " Hp")
                        if tinker.Gethp() <= 0:
                            print("were able to kill the enemies and also kill the tinker!")
                            break
                    if random_ulti == 2:
                        print("You Q in to see if you can hit your ulti but completely fail in hitting any of them and")
                        random_damage_2 = random.randint(40,50)
                        puck.Sethp(puck.Gethp() - random_damage_2)
                        if puck.Gethp() > 0:
                            print("you were able to get away after the mess up but you take quite a bit of damage")
                            time.sleep(2)
                            print("you now have " + puck.Gethp() + " Hp")
                        if puck.Gethp() <= 0:
                            print("and also because you went in and didnt stun any of them they hit you with everything")
                            print("and they kill you")
                            break
                else:
                    print("hopefully you know how to count and noticed this wasn't any of the option's to pick")








        else:
            time.sleep(1)
            print("While you were trying to show off how good you are as " + puck.Getname() + " you failed to notice that ")
            print(tinker.Getname() + " had you on low hp and with that final attack you get to 0 hp and die")
            break








Intro()
Lanegame()

















