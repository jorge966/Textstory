import time
import Dota_2items as item

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
def Earlygame():
    while(True):
        print("The game starts and gavin is seeing what items to buy")
        print("he decides to open a guide to see what other people pick on puck early game")
        for key in enumerate(startingitemsDict):
            values = startingitemsDict(key)
            items = item.items[values[0], values[1]]
            print(str(items))
            break
Earlygame()


















