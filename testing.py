import sys, time, random, json, random

def main():

    Small = "Small Item: [Inventory Empty]"
    Medium = "Medium Item: [Inventory Empty]"
    Large = "Large Item: [Inventory Empty]"

    myJson = {"Small Item:":Small, "Medium Item:":Medium, "Large Item:":Large}
    with open("Inventory.json", "w") as f:
        f.write(json.dumps(myJson))

    Storypath = 100
    r = 0
    aquire = int()

    #Varification Variables
    def z_get() -> int:
        print("")
        slow_type("\nWhat option do you choose (Must be a number):")
        while True:
            try:
                z = int(input(""))
                break
            except: 
                sys.stdout.write("\033[F" + " "*100 + "\r")
                sys.stdout.write("What option do you choose (Must be a number):")
                sys.stdout.flush()
        return z

    def r_get() -> int:
        print("")
        slow_type("\nWhat option do you choose (Must be a number):")
        while True:
            try:
                r = int(input(""))
                break
            except: 
                sys.stdout.write("\033[F" + " "*100 + "\r")
                sys.stdout.write("What option do you choose (Must be a number):")
                sys.stdout.flush()
        return r

    def u_get() -> int:
        print("")
        slow_type("\nWhat option do you choose (Must be a number):")
        while True:
            try:
                u = int(input(""))
                break
            except: 
                sys.stdout.write("\033[F" + " "*100 + "\r")
                sys.stdout.write("What option do you choose (Must be a number):")
                sys.stdout.flush()
        return u

    def SpeChoi_get() -> int:
        print("")
        slow_type("\n(Must be a number): ")
        while True:
            try:
                SpeChoi = int(input(""))
                break
            except: 
                sys.stdout.write("\033[F" + " "*100 + "\r")
                sys.stdout.write("(Must be a number): ")
                sys.stdout.flush()
        return SpeChoi

    #Other Variables
    def game_over():
        typing_speed = 50
        slow_type("\n\nGame Over...")
        typing_speed = 100
        slow_type("\n\nyou feel dreary... as if you had just had a bad dream...\n")
        begin_anew()

    def begin_anew():
        while True:
            r = input("\nWould you like to restart the story?\nContinue or Quit: ")

            capr = str.upper(r)
            if capr == "Continue" or capr == "C":
                main()
            elif capr == "QUIT" or capr == "Q":
                print("\nVerywell Adventurure, shall we meet again...\n")
                exit()
                
            else:
                print("\nPlease answer with continue or Quit...")
            main()
    
    def inventory():
        with open("Inventory.json", "r") as f:
            Data = json.loads(f.read())
            print("------------------------------------")
            print("")
            slow_type(Data["Small Item:"])
            print("\n")
            slow_type(Data["Medium Item:"])
            print("\n") 
            slow_type(Data["Large Item:"])
            print("\n")
            print("------------------------------------")

    def aquire_():
        slow_type("\nDo you wish to add this item to your inventory? (Yes or No): ")
        aquire = input()
        aquire = str.upper(aquire)
        return aquire

    #typing_speed = 500 #Game Speed words per minute
    typing_speed = 1000 #Test Speed words per minute
    def slow_type(t):
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            #time.sleep(1.0*10.0/typing_speed) #Speed for Playing
            time.sleep(1.0*1.0/typing_speed) #Speed for testing

    print()
    slow_type('Welcome to "Anthonys Text Based Game [ATBG]", What is your name? ') 
    x = input()
    print()
    print("Hello",x,"nice to meet you...")

    #Ready to Begin?
    while True:
        slow_type("\nAre you ready to begin now? \nYes or No... ")
        y = input()
        y = str.upper(y)
        if y == "NO" or y == "N":
            slow_type("\nOk then... I guess you'll never witness this epic story...")
        elif y == "YES" or y == "Y":
            break

    slow_type("\n[!Important!]\n\n - (When prompted with a multiple choice number question input the number alone)\n\n - (When prompted with a yes or no type either (y / n) or (yes / No)\n\n----------------------------------------------------------------------------\n\nGreat! The adventure begins... \n\nYou find yourself on a rocky beach, ahead of you there \nis a sandy hill and to your left the remains of crashed \nshipwreck.\n")

    #First Question of the story
    while Storypath == 100: 
        slow_type("\nYou feel an ache in your back as you stand up and you soon \nrelize that you could get a better view of the sourounding\nland if you went up the hill. However you also notice\nsomething glimmering in the hull of the deserted ship.\n\nOption 1: Climb atop the sandy hill\n\nOption 2: Walk into the hull of the broken ship\n\nOption 3: View Inventory (Press 3)")
        z = z_get()

        #First Branch Choice (1 or 2)
        while True:
            if z == 1:
                slow_type("\nYou make your way up the hill with the remaining energy \nyou have and servey the land around you, to your left \nyou see a tent in an open field, Up ahead you see\na forrest and campfire smoke in the distance\n")
                Storypath = 1
                break

            elif z == 2:
                #Description of player actions
                slow_type("\nyou sumble towards the destroyed hull of the ship and reach\nfor the glimmering object and find yourself holding a brass\npocketwatch. The time is 12:30 looking to the far side of the \nbeach you see a man standing there, you also consider climbing \nthe hill and serveying the sourounding area.\n")
                
                #Aquire Item Choice
                aquire = aquire_()
                if aquire == "NO" or aquire == "N":
                    slow_type("\nYou longingly walk away from the brass pocketwatch...\n")
                    Storypath = 2
                    break
                elif aquire == "YES" or aquire == "Y":
                    Small = "Small Item: Brass Pocketwatch"
                    myJson = {"Small Item:":Small, "Medium Item:":Medium, "Large Item:":Large}
                    with open("Inventory.json", "w") as f:
                        f.write(json.dumps(myJson))
                    slow_type("\n+ Brass Pocketwatch (see in inventory)\n")
                    #Story Continuation
                    Storypath = 2
                    break
                
            #Access inventory
            elif z == 3:
                inventory()
                Storypath = 100
                break
                
            else:
                slow_type("\nYou squint your eyes feeling tired\n\n(Remember, The answer must be a number and must correlate to an option)\n")
                break

    #Path 1
    while Storypath == 1:

        time.sleep(0.5)
        slow_type("\nOption 1: Head towards the tent in the field\n\nOption 2: Make your way into the forest\n\nOption 3: Walk past the tent and into the open field\n\nOption 4: View Inventory (Press 4)")
        z = z_get()

        while True:
            if z == 1:
                Storypath = 11
                slow_type("\nYou walk towards the tent, it's desearted but you find \nan old tin box by a long extinguished fire...")
                break

            elif z == 2:
                Storypath = 12
                slow_type("\nYou follow the trail of smoke on the horrizon into the forrest,\nthe world sudenly becomes dark as sunlight becomes shrouded by the tree\ncanopy above, ahead of you is a wooden sign nailed to a tree,\nwith a mysterious arrow pointing left")
                break

            elif z == 3:
                Storypath = 13 
                slow_type("\nYou walk past the tent and then enter the open field, squinting \nyou are able to see a man riding a horse in the \ndistance... he turns and glares at you...")
                break

            #Access inventory
            elif z == 4:
                inventory()
                Storypath = 1
                break

            else:
                slow_type("\nYou squint your eyes feeling tired and colapse onto the ground\n")
                break

    #Sub-storypath (11)
    while Storypath == 11:

        time.sleep(0.5)
        slow_type("\n\nOption 1: open up the tin box and see what's inside\n\nOption 2: try to find something in the extinguished fire\n\nOption 3: Look inside of the tent\n\nOption 4: View Inventory (Press 4)")
        r = r_get()

        while True:
            if r == 1:
                Storypath = 111
                slow_type("\nYou kneel to the ground and slowly open up the tin box \nand find an old dagger, it's been sharpened recently \nand looks like it's in mint contition.\n")
                aquire = aquire_()
                if aquire == "NO" or aquire == "N":
                    slow_type("\nYou close the tin box and set it to the side...\n")
                    Storypath = 2
                    break
                elif aquire == "YES" or aquire == "Y":
                    Medium = "Medium Item: Old Dagger"
                    myJson = {"Small Item:":Small, "Medium Item:":Medium, "Large Item:":Large}
                    with open("Inventory.json", "w") as f:
                        f.write(json.dumps(myJson))
                    slow_type("\n+ Old Dagger (see in inventory)\n")
                    break

            elif r == 2:
                Storypath = 112
                slow_type("\nYou find a chared stick, it looks like it's still hot...\n")
                aquire = aquire_()
                if aquire == "NO" or aquire == "N":
                    slow_type("\nYou throw the stick to the side, What good is it anyways...\n")
                    Storypath = 2
                    break
                elif aquire == "YES" or aquire == "Y":
                    Medium = "Medium Item: Chared Stick"
                    myJson = {"Small Item:":Small, "Medium Item:":Medium, "Large Item:":Large}
                    with open("Inventory.json", "w") as f:
                        f.write(json.dumps(myJson))
                    slow_type("\n+ Chared Stick (see in inventory)\n")
                    break

            elif r == 3:
                Storypath = 113 
                slow_type("\nAs you walk into the tent you find an old rifle hanging from \none of the tent compartments...\n")
                aquire = aquire_()
                if aquire == "NO" or aquire == "N":
                    slow_type("\nYou ignore the old riffle, it's probably broken...\n")
                    Storypath = 2
                    break
                elif aquire == "YES" or aquire == "Y":
                    Large = "Large Item: Old Riffle"
                    myJson = {"Small Item:":Small, "Medium Item:":Medium, "Large Item:":Large}
                    with open("Inventory.json", "w") as f:
                        f.write(json.dumps(myJson))
                    slow_type("\n+ Old Riffle (see in inventory)\n")
                    break

            elif r == 4:
                inventory()
                Storypath = 11
                break

            else:
                slow_type("\nYou squint your eyes feeling tired and colapse onto the ground\n")
                break

    #Sub-Sub-Storypaths (111 & 112)
    while Storypath == 111 or Storypath == 112:

        time.sleep(0.5)
        slow_type('\n[!Event!]\n\nAs you are putting the item away for safe keeping\na man rides towards you at full speed, quickly\njumps of of his horse and yells\n\n"Put your hands in the air! This is an ambush!"\n\nOption 1: Hand the man all items inside your inventory\n\nOption 2: Select an item from inventory (Preferably a weapon)')
        u = u_get()

        while True:
            if u == 1:
                typing_speed = 200
                slow_type('\nAt first you are shocked but you decide that it is \nbest to give the theif everything you have.\n\n - (all items in inventory)\n\nAt first you are relieved but then relize the man is \nstill pointing his weapon at you...\n\nTheif: "I can not risk letting you out alive"')
                game_over()
                break

            elif u == 2:
                inventory()
                slow_type("Which size of Item whould you like to use? (Small, Medium or Large)\n\nEnter Size here: ")
                use = input()
                use = str.upper(use)
                if use == "SMALL" or use == "S":
                    slow_type("\nYou reach for a small item but soon relize theres nothing there... A tragic fate...")
                    game_over()
                if use == "MEDIUM" or use == "M":
                    if Medium == "Medium Item: Old Dagger":
                        slow_type("\nYou pull out the rusty old dagger that you had recently aquired and\nthrust it at the theif agreesively... the theif's eyes widen and \nrealizes he's been hit... he drops his weapon and runs away...\n\n...Phew that was close...\n\n[Event Concluded]")
                        Storypath = 10000
                        break

                    if Medium == "Medium Item: Chared Stick":
                        slow_type("\nyou pull out the chared stick you had recently picked up from the\nnow extinguished campfire... you wave it at the theif and a smell of\nsmoke fills the air... It seems the theif has a severe alergic reaction to\nthe smell and collapses to the ground\n\n...Phew that was close...\n\n[Event Concluded]")
                        Storypath = 10000
                        break

                if use == "LARGE" or use == "L":
                    slow_type("\nYou reach for a large item but soon relize theres nothing there... A tragic fate...")
                    game_over()
                    break

            else:
                slow_type("\nYou squint your eyes feeling tired and colapse onto the ground\n")
                break
    #Sub-Sub-Storypath (113)
    while Storypath == 113:

        time.sleep(0.5)
        slow_type('\n[!Event!]\n\nAs you are putting the riffle away for safe keeping\nyou hear a man entering the tent from behind, quickly\nyou turn around and find yourself looking at a theif \nholding a blade towards you...\n\n"Put your hands in the air! This is an ambush!"\n\nOption 1: Hand the man all items inside your inventory\n\nOption 2: Select an item from inventory (Preferably a weapon)')
        u = u_get()

        while True:
            if u == 1:
                typing_speed = 200
                slow_type('\nyou reluctantly hand over everything you have...\n\n - (all items in inventory)\n\nTheif: "Sorry Partner... I simply can not risk letting you out alive"')
                game_over()
                break

            elif u == 2:
                inventory()
                slow_type("Which size of Item whould you like to use? (Small, Medium or Large)\n\n(if you choose to use a weapon there is only a 50 percent chance you'll make it out alive) Enter Size here: ")
                use = input()
                use = str.upper(use)
                if use == "SMALL" or use == "S":
                    slow_type("\nYou reach for a small item but soon relize theres nothing there... A tragic fate...")
                    game_over()
                if use == "MEDIUM" or use == "M":
                    slow_type("\nYou reach for a medium item but soon relize theres nothing there... A tragic fate...")
                    game_over()
                if use == "LARGE" or use == "L":
                    if Large == "Large Item: Old Riffle":
                        
                        if random.randint(0,100) < 50:
                            slow_type("\nYou fire the riffle but you fail to aim misserably... A tragic fate...")
                            game_over()
                            break
                        if random.randint(0,100) > 50:
                            slow_type("\nYou fire the riffle and by a stroke of luck the shot successfully\nfree's you from what otherwise would have meant certain death...")
                            Storypath = 10000
                            break

            else:
                slow_type("\nYou squint your eyes feeling tired and colapse onto the ground\n")
                break

    #Sub-storypath (12)
    while Storypath == 12:

        time.sleep(0.5)
        slow_type("\n\nOption 1: Continue walking into the forrest following the \nsmokey trail above the trees\n\nOption 2: Follow the mysterious arrow out of the forrest\n\nOption 3: View Inventory (Press 3)")
        r = r_get()


        while True:
            if r == 1:
                Storypath = 121
                slow_type("\nYou continue to walk into the dark woods following the \ntrail of smoke above the trees. Soon you emerge into a clearing...\nit's gotten dark and ahead of you is an decaying old house... the\nsource of the smoke is a cauldron bubbling with green liquid.\n")
                aquire = aquire_()
                if aquire == "NO" or aquire == "N":
                    slow_type("\nYou ignore the strange green liquid, it probably tastes disguisting...\n")
                    Storypath = 2
                    break
                elif aquire == "YES" or aquire == "Y":
                    Small = "Small Item: Green Potion"
                    myJson = {"Small Item:":Small, "Medium Item:":Medium, "Large Item:":Large}
                    with open("Inventory.json", "w") as f:
                        f.write(json.dumps(myJson))
                    slow_type("\n+ Green Potion (see in inventory)\n")
                    break

            elif r == 2:
                Storypath = 122
                slow_type("\nyou exit the story and realize that it's gotten very dark.\nAhead of you there is a small green man (goblin) holding\na twisted dager\n\nPrepare to engage in combat.")
                break

            elif r == 3:
                inventory()
                Storypath = 12
                break

            else:
                slow_type("\nYou squint your eyes feeling tired and colapse onto the ground\n")
                break

    #Sub-Sub-Storypath (121)
    while Storypath == 121:
        time.sleep(0.5)
        slow_type('\n[!Event!]\n\nAs you are are standing there debating your next course of action\na plume of smoke appears and a robed person apears\n\n"(Screechy voice) This is my land! Be gone!"\n\n[engaged in combat]\n\nOption 1: Run away!\n\nOption 2: Select an item from inventory (Preferably a weapon)')
        u = u_get()

        while True:
            if u == 1:
                typing_speed = 200
                slow_type('\nyou make a run for it and barely make it out of the forrest alive\nyou are panting and nearly compleately out of breath when all\nof a sudden you see another plume of smoke...\n\n"You can never run away from me!"\n\nA tragic fate...')
                game_over()
                break

            elif u == 2:
                inventory()
                slow_type("Which size of Item whould you like to use? (Small, Medium or Large)\n\nEnter Size here: ")
                use = input()
                use = str.upper(use)
                if use == "SMALL" or use == "S":
                    if Small == "Small Item: Green Potion":
                        slow_type("\nYou hold the green potion in your hand... now it is up to you...\n\nOption 1: Drink the potion (100 percent chance it will work)\n\nOption 2: Throw the potion at the enemy (70 percent chance it will work)")
                        SpeChoi_get()

                        if SpeChoi == 1:
                            slow_type("\nYou drink the potion and soon regret it, your body aches and you collapse... A terrible fate")
                            game_over()
                        
                        if SpeChoi == 2:
                            if random.randint(0,100) < 30:
                                slow_type("\nYou throw the potion but fail to aim misserably and end up dropping it on yourself... A tragic fate...")
                                game_over()
                                break
                            if random.randint(0,100) > 30:
                                slow_type("\nThe potion flies through the air and strikes the wizard like enemy\nthey screetch in horror and fall to the ground melting into\na strange magic puddle...")
                                Storypath = 10000
                                break

                if use == "MEDIUM" or use == "M":
                    slow_type("\nYou reach for a Medium item but soon relize theres nothing there... A tragic fate...")
                    game_over()
                if use == "LARGE" or use == "L":
                    slow_type("\nYou reach for a large item but soon relize theres nothing there... A tragic fate...")
                    game_over()
                break

            else:
                slow_type("\nYou squint your eyes feeling tired and colapse onto the ground\n")
                break
    #Sub-Sub-Storypath (122)
    while Storypath == 122:
        time.sleep(0.5)
        slow_type('\n\n[!Event!]\n\nYou seem to have come face to face with an unexpected foe...\nthe goblin like creature addresses you...\n\n"(goblin voice) Garble-gablarb! Baflubba-Chubb-Habba!"\n\n(you cannot understand the unfamiliar language)\n\n[engaged in combat]\n\nOption 1: Run away, Run as fast as you can!\n\nOption 2: Select an item from inventory (Preferably a weapon)')
        u = u_get()

        while True:
            if u == 1:
                typing_speed = 200
                slow_type('\nyou make a run for it and barely make it out of the forrest alive\nyou are panting and nearly compleately out of breath when all\nof a sudden your see hundreds more goblins in front of you \n\n(Unintelegable)"Grabble-chabba Bahgoom!"\n\n[you are defeated by the goblin horde]\n\nA tragic fate...')
                game_over()
                break

            elif u == 2:
                inventory()
                slow_type("you have no items... choose something anyways... (Small, Medium or Large)\n\nEnter Size here: ")
                use = input()
                use = str.upper(use)
                if use == "SMALL" or use == "S" or use == "MEDIUM" or use == "M" or use == "LARGE" or use == "L":
                        slow_type("\nAlthough there is nothing in your hands there still may be a way out of this...\n\nOption 1: Fist fight out of this...\n\nOption 2: Attempt to communicate through sign language (50 percent chance it will work)\n\n(answer must be a number) ")
                        SpeChoi = int(input())
                        
                        if SpeChoi == 1:
                            slow_type("\nYou attempt to fight the gobblin but hundreds begin to flood out of the bushes,\nit becomes to much to handle... A terrible fate")
                            game_over()
                        
                        if SpeChoi == 2:
                            if random.randint(0,100) < 50:
                                slow_type("\nYou attempt using sign language to communicate with the beast...\n\nIt seems insulted...\n\nA tragic fate...")
                                game_over()
                                break
                            if random.randint(0,100) > 50:
                                slow_type("\nAfter a few minutes of negotiating you bid your new friend goodbye and go on your way...")
                                Storypath = 10000
                                break


            else:
                slow_type("\nYou squint your eyes feeling tired and colapse onto the ground\n")
                break

    #Sub-Storypath (13)
    while Storypath == 13:

        time.sleep(0.5)
        slow_type("\n\nOption 1: Walk towards the man on the horse (maybe he has something to say)\n\nOption 2: Walk away from the man and walk the oposite direction as him\n\nOption 3: View Inventory (Press 3)")
        r = r_get()


        while True:
            if r == 1:
                Storypath = 131
                slow_type('\nYou walk up to the man and he stares down at you... \n\n"what do you want stranger!" (angry tone)\n\n[man pulls out sword]')
                break

            elif r == 2:
                Storypath = 132
                slow_type('\nyou walk away trying not to make eye contact when you\nhear somone yell to you... "Hey! Come back here"')
                break

            elif r == 3:
                inventory()
                Storypath = 13
                break

            else:
                slow_type("\nYou squint your eyes feeling tired and colapse onto the ground\n")
                break
    #Sub-Sub-Storypath (131 & 132)
    while Storypath == 131 or Storypath == 132:

        time.sleep(0.5)
        slow_type('\n\n[!Event!]\n\n*The man get unmounts his horse*\n\nHorseman: "Listen partner... I do not recognise you..."\n\n"I want to know who you think you are, there have been many\ntheives around these parts recently and I cannot be sure who to trust..."\n\nOption 1: Tell the man you are a lost adventurure\n\nOption 2: Tell the man you are a castaway\n\nOption 3: Tell the man you are a theif\n\nOption 4: Select an item from inventory (Preferably a weapon)')
        u = u_get()

        while True:
            if u == 1 or u == 2:
                Storypath = 10000
                slow_type('\nHorseman: "Ah, I see! My most senscire appology..."\n\n"Here, take this, for your travels"\n\n(The Horseman hands you magic spellbook)\n')
                aquire = aquire_()
                if aquire == "NO" or aquire == "N":
                    slow_type("\nYou refuse it, it's probably is full of gibberish...\n")
                    break
                elif aquire == "YES" or aquire == "Y":
                    Large = "Large Item: Magic Book"
                    myJson = {"Small Item:":Small, "Medium Item:":Medium, "Large Item:":Large}
                    with open("Inventory.json", "w") as f:
                        f.write(json.dumps(myJson))
                    slow_type("\n+ Magic Book (see in inventory)\n")
                    break

            elif u == 3:
                typing_speed = 200
                slow_type('\nThe words theif barely make it out of your mouth and the horseman\nbegins to thrust his blade at you in a fever like state\n\n[You are severely Wounded!]"\n\nA tragic fate...')
                game_over()
                break

            elif u == 4:
                inventory()
                slow_type("you have no items... choose something anyways... (Small, Medium or Large)\n\nEnter Size here: ")
                use = input()
                use = str.upper(use)
                if use == "SMALL" or use == "S" or use == "MEDIUM" or use == "M" or use == "LARGE" or use == "L":
                        slow_type("\nAlthough there is nothing in your hands there still may be a way out of this...\n\nOption 1: Fight the horseman...\n\nOption 2: Distract the man and run away (50 percent chance it will work)\n\n(answer must be a number) ")
                        SpeChoi = int(input())
                        
                        if SpeChoi == 1:
                            slow_type("\nYou attempt to fight the Horseman...\n\nYou soon learn that it's imposable to punch yourself out of a swordfight\n\n... A terrible fate")
                            game_over()
                        
                        if SpeChoi == 2:
                            if random.randint(0,100) < 50:
                                slow_type('\nYou attempt to distract the man by pointing at a tree and saying, "is that spruce wood?"\n\nHe seems insulted by your foolishness...\n\nA tragic fate..')
                                game_over()
                                break
                            if random.randint(0,100) > 50:
                                slow_type('\nYou distract the mn by pointing behind him and yelling "Run! Bandits"\n\n[The man runs away shrieking in fear]')
                                Storypath = 10000
                                break
                    
    #Path 2
    while Storypath == 2:
        time.sleep(0.5)
        slow_type("\nOption 1: stay were you are continue investigation the hull \nof the ship\n\nOption 2: make your way towards the man on the far side of the beach \n(maybe he has something to say)\n\nOption 3: Run along the other side of the beach and get out of \nthere\n\nOption 4: View Inventory (Press 4)")
        z = z_get()

        while True:
            if z == 1:
                Storypath = 21
                slow_type("\nInside of the hull you find the deceased body of who you \nremember as the captian of the ship, In his pocket is a revolver.\n")
                aquire = aquire_()
                if aquire == "NO" or aquire == "N":
                    slow_type("\nYou ignore the decorated revolver, it doesn't belong to you...\n")
                    Storypath = 2
                    break
                elif aquire == "YES" or aquire == "Y":
                    Medium = "Medium Item: Captains Revolver"
                    myJson = {"Small Item:":Small, "Medium Item:":Medium, "Large Item:":Large}
                    with open("Inventory.json", "w") as f:
                        f.write(json.dumps(myJson))
                    slow_type("\n+ Captains Revolver (see in inventory)\n")
                    break

            elif z == 2:
                Storypath = 22
                slow_type("\nYou sprint as fast as you can towards the man on the beach\nhe's rather starteled at first but then started talking.\n\n")
                slow_type('"Who in the world are you?!"')
                break

            elif z == 3:
                Storypath = 23
                slow_type("\nYou sprint across the other side of the beach and come\nacross a small beachside shack. ")
                break

            elif z == 4:
                inventory()
                Storypath = 2
                break

            else:
                slow_type("\nYou squint your eyes feeling tired and colapse onto the ground\n")
                break

    #Sub-Storypaths (21)
    while Storypath == 21:

        time.sleep(0.5)
        slow_type("\nOption 1: Examine his revolver\n\nOption 2: Examine the body for more loot\n\nOption 3: Exit the ship out of fear\n\nOption 4: View Inventory (Press 4)")
        r = r_get()

        while True:
            if r == 1:
                Storypath = 211
                slow_type("\nYou kneel examine the revolver, it has a beatiful engraving on the\n handle stock and apon further inspection 3 rounds")
                break

            elif r == 2:
                Storypath = 212
                slow_type("\nYou find nothing else, it seems that all that was on the captain\ndrifted off into the ocean...")
                break

            elif r == 3:
                Storypath = 213 
                slow_type("\nThe sight of the dead captain makes your stomache cramp and you \nfeel the need to run outside to get fresh air... as you emerge \nfrom the hull you notice a man is standing in front of you... he\n tells you to hand over what you found in the ship while pointing\n a dull blade at you")
                break

            elif r == 4:
                inventory()
                Storypath = 21
                break

            else:
                slow_type("\nYou squint your eyes feeling tired and colapse onto the ground\n")
                break
    #Sub-Sub-Storypaths (211 & 212)
    while Storypath == 211 or Storypath == 212:
        time.sleep(0.5)
        slow_type('\n\n[!Event!]\n\nAs you are are standing there you hear the click of a revolver \nbehind your head...\n\nTheif: "Hand everything over!"\n\nOption 1: Do as he says...\n\nOption 2: Select an item from inventory (Preferably a weapon)')
        u = u_get()

        while True:
            if u == 1:
                typing_speed = 200
                slow_type('\nAt first you are shocked but you decide that it is \nbest to give the theif everything you have.\n\n - (all items in inventory)\n\... The man is \nstill pointing his weapon at you...\n\nTheif: "I can not risk letting you out alive"\n\n A Tragic Fate...')
                game_over()
                break

            elif u == 2:
                inventory()
                slow_type("Which size of Item whould you like to use? (Small, Medium or Large)\n\nEnter Size here: ")
                use = input()
                use = str.upper(use)
                if use == "SMALL" or use == "S":
                    if Small == "Small Item: Brass Pocketwatch":
                        slow_type("\nYou hold the Pocketwatch in your hand... now it is up to you...\n\nOption 1: Press a small button on the watch (100 percent chance it will work)\n\nOption 2: Tell the theif the time (30 percent chance it will work)\n\n(answer must be a number) ")
                        SpeChoi = int(input())
                        
                        if SpeChoi == 1:
                            Storypath = 10000
                            slow_type("You start to twist a small button on the watch and the hands start \nto move backwards... However all time an space around you begins to\nwarp without end... The world spins in on itslef and collapses... where am I? ")
                            break
                        
                        if SpeChoi == 2:
                            if random.randint(0,100) < 30:
                                slow_type("\nYou tell the theif the time and he leaves as fast as he appered,\n looks like he had a train to catch....")
                                Storypath = 10000
                                break
                            if random.randint(0,100) > 30:
                                slow_type("\nYou tell the theif it's 12:30... The theif laughs at you... A Tragic fate...")
                                game_over()
                                break

                if use == "MEDIUM" or use == "M":
                    if Medium == "Medium Item: Captains Revolver":
                        slow_type("\nYou hold the revolver in your hand... now it is up to you...\n\nOption 1: Juggle the revolver and it's rounds as a distraction\n\nOption 2: fire the revolver\n\n(answer must be a number) ")
                        SpeChoi = int(input())
                        
                        if SpeChoi == 1:
                            slow_type("You start juggling but the theif seems unphased... well looks like theres no way out... A tragic fate :/")
                            game_over()
                        
                        if SpeChoi == 2:
                            slow_type("\nYou fire the revolver and the theif drops to the ground after only one round was fired...\n\n - 1 revolver round")
                            Storypath = 10000
                            break
                
                if use == "LARGE" or use == "L":
                    slow_type("\nYou reach for a large item but soon relize theres nothing there... A tragic fate...")
                    game_over()
                break
    #Sub-Sub-Storypath (213)
    while Storypath == 213:
        time.sleep(0.5)
        slow_type('\n\n[!Event!]\n\nAs you are are standing there you hear the click of his revolver \n\nTheif: "Like I said, Hand everything over!"\n\nOption 1: Do as he says...\n\nOption 2: Select an item from inventory (Preferably a weapon)')
        u = u_get()

        while True:
            if u == 1:
                typing_speed = 200
                slow_type('\nAt first you are shocked but you decide that it is \nbest to give the theif everything you have.\n\n - (all items in inventory)\n\... The man is \nstill pointing his weapon at you...\n\nTheif: "I can not risk letting you out alive"\n\n A Tragic Fate...')
                game_over()
                break

            elif u == 2:
                inventory()
                slow_type("Which size of Item whould you like to use? (Small, Medium or Large)\n\nEnter Size here: ")
                use = input()
                use = str.upper(use)
                if use == "SMALL" or use == "S":
                    if Small == "Small Item: Brass Pocketwatch":
                        slow_type("\nYou hold the Pocketwatch in your hand... now it is up to you...\n\nOption 1: Press a small button on the watch (100 percent chance it will work)\n\nOption 2: Tell the theif the time (30 percent chance it will work)\n\n(answer must be a number) ")
                        SpeChoi = int(input())
                        
                        if SpeChoi == 1:
                            Storypath = 10000
                            slow_type("You start to twist a small button on the watch and the hands start \nto move backwards... However all time an space around you begins to\nwarp without end... The world spins in on itslef and collapses... where am I? ")
                            break
                        
                        if SpeChoi == 2:
                            if random.randint(0,100) < 30:
                                slow_type("\nYou tell the theif the time and he leaves as fast as he appered,\n looks like he had a train to catch....")
                                Storypath = 10000
                                break
                            if random.randint(0,100) > 30:
                                slow_type("\nYou tell the theif it's 12:30... The theif laughs at you... A Tragic fate...")
                                game_over()
                                break

                if use == "MEDIUM" or use == "M":
                    if Medium == "Medium Item: Captains Revolver":
                        slow_type("\nYou hold the revolver in your hand... now it is up to you...\n\nOption 1: Juggle the revolver and it's rounds as a distraction\n\nOption 2: fire the revolver\n\n(answer must be a number) ")
                        SpeChoi = int(input())
                        
                        if SpeChoi == 1:
                            slow_type("You start juggling but the theif seems unphased... well looks like theres no way out... A tragic fate :/")
                            game_over()
                        
                        if SpeChoi == 2:
                            slow_type("\nYou fire the revolver and the theif drops to the ground after only one round was fired...\n\n - 1 revolver round")
                            Storypath = 10000
                            break
                
                if use == "LARGE" or use == "L":
                    slow_type("\nYou reach for a large item but soon relize theres nothing there... A tragic fate...")
                    game_over()
                break

    #Sub-Storypaths (22)
    while Storypath == 22:

        time.sleep(0.5)
        slow_type('\n\nOption 1: "I am cornelius"\n\nOption 2: "It seems I can ask you the same question..."\n\nOption 3: View Inventory (Press 3)')
        r = r_get()

        while True:
            if r == 1:
                Storypath = 221
                slow_type('\n"Cornelius... The man who killed my son!? I have \nbeen waiting for this moment for years... En Gard!"')
                break

            elif r == 2:
                Storypath = 222
                slow_type('\n"answering a question with a question huh, \nI like that sprit, here have this..."')
                break

            elif r == 3:
                inventory()
                Storypath = 22
                break

            else:
                slow_type("\nYou squint your eyes feeling tired and colapse onto the ground\n")
                break
    #Sub-Sub-Storypath (221)
    while Storypath == 221:

        time.sleep(0.5)
        slow_type('\n\n[!Event!]\n\nIt seems that this stranger has mistaken you for the killer of\nhis son..."\n\nOption 1: attempt to explain yourself\n\nOption 2: Select an item from inventory (Preferably a weapon)')
        u = u_get()

        while True:
            if u == 1:
                typing_speed = 200
                slow_type('\nyou attmept to tell the man who you trully are but he\nrefuses to listen to you... All he says is\n\nStranger: "Cornelius! You Monster!"\n\n...you are unable to escape the wrath of the stranger\n\nA tragic fate...')
                game_over()
                break

            elif u == 2:
                inventory()
                slow_type("Which size of Item whould you like to use? (Small, Medium or Large)\n\nEnter Size here: ")
                use = input()
                use = str.upper(use)
                if use == "SMALL" or use == "S":
                    if Small == "Small Item: Brass Pocketwatch":
                        slow_type("\nYou pull out the Brass Pocketwatch from your pocket...\n\nAfter twisting the time knob the watch hands begin to go backwards\nbut to your surprize so does time itself... The man says everything he\nhad said to you before but this time backwards and walked away\n*You thinking: Strange...*\n\n[Event Concluded]")
                if use == "MEDIUM" or use == "M":
                    slow_type("\nYou reach for a medium item but soon relize theres nothing there... A tragic fate...")
                    game_over()
                if use == "LARGE" or use == "L":
                    slow_type("\nYou reach for a large item but soon relize theres nothing there... A tragic fate...")
                    game_over()
                    Storypath = 10000
                    break
    #Sub-Sub-Storypath (222)
    while Storypath == 222:

        time.sleep(0.5)
        slow_type('\n\n[!Event!]\n\nThe man hands you an old tome (old book)\n\nOption 1: Read the first page')
        u = u_get()

        while True:
            if u == 1:
                Storypath = 10000
                slow_type('\nYou glide your finger to find the words on the first page. Once\nthe words have been found you read this to yourself:\n\nIn criptic words it states: "In case you one day begin anew... and thou fortunes few... The green couldron should be nothing new... 1-2-1')
                break

    #Sub-Storypaths (23)
    while Storypath == 23:

        time.sleep(0.5)
        slow_type('\nOption 1: Walk into the beachside shack, (there may be something, or someone inside)\n\nOption 2: Walk to the back of the shack, maybe something is behind...\n\nOption 3: View Inventory (Press 3)')
        r = r_get()

        while True:
            if r == 1:
                Storypath = 231
                slow_type('\nyou open the door and it creaks opens slowly\nnobody is home but you hear sombody approaching from \noutside of the house...')
                break

            elif r == 2:
                Storypath = 232
                slow_type('\nYou walk to the back of the shack and find a \nred potion lying beside a bunch of lab equiptment.\n')
                aquire = aquire_()
                if aquire == "NO" or aquire == "N":
                    slow_type("\nYou ignore the Red Potion...\n")
                    Storypath = 2
                    break
                elif aquire == "YES" or aquire == "Y":
                    Small = "Small Item: Red Potion"
                    myJson = {"Small Item:":Small, "Medium Item:":Medium, "Large Item:":Large}
                    with open("Inventory.json", "w") as f:
                        f.write(json.dumps(myJson))
                    slow_type("\n+ Red Potion (see in inventory)\n")
                    break

            elif r == 3:
                inventory()
                Storypath = 23
                break

            else:
                slow_type("\nYou squint your eyes feeling tired and colapse onto the ground\n")
                break
    #Sub-Sub-Storypaths (231 & 232)
    while Storypath == 231 or Storypath == 232:
    
        time.sleep(0.5)
        slow_type('\n[!Event!]\n\nFrom behind you, you feel sombody has entered the vacinity, then you hear a voice\n\nThe voice: "Who are you?!"\n\nOption 1: turn around and give the person everything inside your inventory\n\nOption 2: Select an item from inventory (Preferably a weapon)')
        u = u_get()

        while True:
            if u == 1:
                Storypath = 10000
                slow_type('\nyou turn around to find an old lady and reluctantly hand over everything you have...\n\n - (all items in inventory)\n\nShe is rather confused but accepts graciously...')
                break

            elif u == 2:
                inventory()
                slow_type("Which size of Item whould you like to use? (Small, Medium or Large)\n\n(if you choose to use a weapon there is only a 50 percent chance you'll make it out alive) Enter Size here: ")
                use = input()
                use = str.upper(use)
                if use == "SMALL" or use == "S":
                    if Small == "Small Item: Red Potion":
                            slow_type("\nYou drink the red potion and turn invisable, by now you've\nfigured out that whoever was behind you was just a defenceless\nold lady but at least you escaped from the situation...")
                            Storypath = 10000
                            break
                    if Small == "Small Item: Brass Pocketwatch":
                            slow_type("\nYou turn around and find yourself looking at a defenceless\nold lady, you tell her the time, have tea with her and then leave alive and well...")
                            Storypath = 10000
                            break
                if use == "MEDIUM" or use == "M":
                    slow_type("\nYou reach for a medium item but soon relize theres nothing there... A tragic fate...")
                    game_over()
                if use == "LARGE" or use == "L":
                    slow_type("\nYou reach for a Large item but soon relize theres nothing there... A tragic fate...")
                    game_over()

    #The End
    while Storypath == 10000:
        slow_type("\n\nImpressive... You made it to the end of the Game!\n\nFeel free to replay the game and discover every unique scenario!")
        begin_anew
        break

main()
