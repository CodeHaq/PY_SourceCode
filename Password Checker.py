from getpass import getpass
import time
from os import system, name
import stdiomask
import random
  

def clear():
    if name == 'nt':
        _ = system('cls')
  

def rules():
        rules = ["If you press 1, you have a chance to hit a fighter plane", "If you press 0, you dodge and have a chance to regenerate 1 life",
                 "you have 2 lives but ammo and fighter planes depend on level.", "Ok lets start."]
        for rule in rules:
            input(rule)


def randox(a, b):
        from random import seed
        from random import randint
        for _ in range(1):
            value = randint(a, b)
        return value


def endgame(Score, ammo, Fighter_planes):
    if ammo == 0 and Fighter_planes > 0:
        print("Mission failed, ammo ran out.")
        print(Score, "score")
    elif Fighter_planes > 0:
        print("You Lose with", Score,
                "score. Nice try!")
        return
    else:
        print("You Win with", Score,
                "score. Great Job!")
        return
    

clear()
ren = 0
pword = 0
Req = 0
password_status = 'Bad'

first_identify = input("Do you have an account: ")

while first_identify != 'yes' and first_identify != 'no':
    print('Invalid Input!')
    print()
    first_identify = input("Do you have an account: ")

while True:
    if first_identify == 'yes':
        print('Please enter your Username and Password:')
        print()
        username = input('Username = ')
        password = stdiomask.getpass('Password = ', '*')
        try:
            user_test = username + '.txt'
            with open(user_test, 'r') as rango:
                for line in rango:
                    if username in line :
                        continue
                    elif password in line:
                        print('Welcome, {}!'.format(username))
                        break
                else:
                    print("Incorrect password")
                    answere = input("If you don't know your password please create a new account (y/n): ")
                    continue
                    # print('You seem to have forgoten your password')
                    # time.sleep(.5)
                    # print("If you don't remeber it please create a new account.")
                    # first_identify = 'no'
            
        except:
            print("This account does not exist, please create a new account")
            first_identify = 'no'

print()

if first_identify == 'no':
    print('Please create a Username and secure Password with a number, special character and a capital.')
    while password_status != 'strong':        
        username = input('Username = ')
        password = stdiomask.getpass('Password = ', '*')
        
        show_password = input("Press '*' if you would like to see your password: ")
        if show_password == '*':
            print(password, end='\r')
            time.sleep(1)
        user_test = username + '.txt'
        try:
            with open(user_test, 'r') as file:
                for line in file:
                    if username in line:
                        print('Sorry this Username has already been taken,')
                        print('Please enter a new one.')
                        ren += 1
            if ren > 0:
                continue
        except:
            while True:
                Req = 0
                if pword > 0:
                    password = stdiomask.getpass('Password = ', '*')
                
                    show_password = input("Press '*' if you would like to see your password: ")
                    if show_password == '*':
                        print(password, end='\r')
                        time.sleep(1)
                    
                    print()
                
                print('Now checking your password... ')
                    
                requirements = {'Number':('1', '2', '3', '4', '5', '6', '7', '8', '9'), 
                                'Special Char':('!', '@', "#", '%', '^', '&', '*', '_', '-', '+', '=', '<', '>', '?', '/', '|', '\\'),
                                'Capital':('A', 'B', 'C', 'D', 'E' 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')}
                
                
                for char in requirements['Number']:
                    for character in password:
                        if character == char:
                            print("You have a number in your password.")
                            Req += 1
                            break
                    if Req == 1:
                        break
                            
                    
                    
                else:
                    if Req == 0:
                        print("You don't have a number in your password.")
                        pword += 1
                        continue

                time.sleep(1)
                for char in requirements['Special Char']:
                    for character in password:
                        if character == char:
                            print("You have a special character in your password.")
                            Req += 1
                            break
                    if Req == 2:
                        break        
                    
                else:
                    if Req == 1:
                        pword += 1
                        print("You don't have a special character in your password.")
                        continue
                
                time.sleep(1)
                for char in requirements['Capital']:
                    for character in password:
                        if character == char:
                            print("You have a capital letter in your password.")
                            Req += 1
                            break
                    if Req == 3:
                        break        
                else:
                    if Req == 2:
                        pword += 1
                        print("You don't have a capital letter in your password.")
                        continue
                
                break

            print('To continue, please Login: ')
            user_account = username, password
            with open(f'{username}.txt', 'w') as account:
                for item in user_account:
                    print(item, file=account)
                    
            Username_login = input("")
            Password_login = stdiomask.getpass("")
            
            break







Score = 0
health = max = 2
drango1 = 3
drango2 = 3
P1health = 3
P2health = 3
P1ammo = 5
P2ammo = 5
P1value = 0
P2value = 0
Guest_score = 0
P1dodge = 0
P2dodge = 0
games = ["Hangman", 'Fighter plane', 'Guessing game', 'Task game']

question = input("Would you like to play a game? ")
print()

while True:    
    while question != "yes" and question != "no":
        print('Invalid input.')
        question = input("Would you like to play a game? ")
        print()
    if question == 'yes':
        print("What game would you like to play? ")
        for index, game in enumerate(games):
            print("{}: {}".format(index + 1, game))
        game_type = input()
        print()
        if game_type == '3':
            h = 1000
            answer = random.randint(1, h)
            guess = 0   # TODO: Remove after testing
            print("Please guess a number between 1 and {}: ".format(h))

            while guess != answer:
                guess = int(input())
                
                if guess == 0:
                    break
                if guess == answer:
                    print("Well done, you guessed it")
                    break
                else:
                    if guess < answer:
                        print("Please guess higher")
                    else:
                        print("Please guess lower")
        
        if game_type == '4':
            import random
            import time
            from Colour_print import GREEN, RED, BLUE, YELLOW, CYAN, MAGENTA, colour_print
            import colorama


            def randox(a, b):
                from random import seed
                from random import randint
                for _ in range(1):
                    value = randint(a, b)
                return value


            def del_task(list, value):
                for index in range(len(list) - 1, -1, -1):
                    if list[index] == value:
                        del list[index]


            alltasks = 0


            print("")
            print("Among us, Booting up!")
            renew_id = 0
            time.sleep(1)
            Commontasks = ['Enter ID, ', 'Fix wiring, ']
            longtasks = ['Upload data, ', 'Start reactor, ', 'Inspect sample, ',
                        'Fuel engines, ']
            shorttasks = ['Clean O2, ', 'Defences, ', 'Sheilds, ',
                        'Stabilize steering, ', 'Unlock manifolds, ']
            othertasks = ['Empty Garbage, ', 'Chart course, ',
                        'Divert power, ', 'Submit scan, ']
            task1 = random.choice(Commontasks)
            task2 = random.choice(longtasks)
            task3 = random.choice(shorttasks)
            task4 = random.choice(othertasks)
            print('')
            print("These are your tasks;", task1, task2, task3, task4)
            all_tasks = [task1, task2, task3, task4]
            upload = None
            Div_power = None
            while alltasks != 4:
                print("")
                loc = input(
                    "Where would you like to go? Admin, Storage, 02, Reactor, Nav., Weapons, Med bay, Elec. or Engines: ")

                if loc == "Admin":

                    print('')
                    print('Welcome to Admin')
                    time.sleep(1)
                    print('')
                    if task1 == "Enter ID, " and task1 in all_tasks:

                        print('This is the Enter ID task, please enter the number given.')
                        time.sleep(1)
                        print('')
                        vart = randox(10000, 99999)
                        print("You have 6 seconds to complete this task.")
                        time.sleep(1.5)
                        print(vart)
                        print('')

                        import time
                        from threading import Thread
                        swipe = None

                        def check():
                            time.sleep(6)
                            if swipe != None:
                                return
                            else:
                                print("Too Slow")
                                print('Try again!')
                                return
                        Thread(target=check).start()
                        swipe = int(input(""))

                        if vart == swipe:
                            print('Task complete!')
                            del_task(all_tasks, task1)

                            alltasks += 1
                        else:
                            print('')
                            while vart != swipe:
                                vart = randox(10000, 99999)
                                print(vart)
                                swipe = int(input(""))
                                if vart == swipe:
                                    alltasks += 1
                                    del all_tasks[0]
                                    print(all_tasks)
                                    print('Task complete!')
                                    break

                    if task2 == "Upload data, " and task2 in all_tasks:

                        time.sleep(2)
                        print('This is the Downloading Data task.')
                        print('')
                        print('Please wait!')
                        xt = 20
                        while xt != 117:
                            print('')
                            if xt == 105:
                                xt = xt - 5
                            import time
                            print(xt, "% ...")
                            xt = xt + 17
                            time.sleep(2)
                        uploadpoint = ["Cafetria!", 'Elec.', 'Nav.', 'Weapons!']
                        upload = random.choice(uploadpoint)
                        del_task(all_tasks, task2)
                        print('Please upload data at', upload)

                    if Div_power == 'Admin':
                        ac = input('Please accept Diverted power: ')
                        if ac == 'Accept diverted power':
                            alltasks += 1
                            print('Task Complete!')
                    if renew_id == 1:
                        print('Please wait while your ID gets renewed')
                        time.sleep(1)
                        alltasks += 1
                        print('ID is renewed')

                    else:
                        print('')
                        time.sleep(2)
                        print('You have no more tasks here.')

                if loc == "Elec.":
                    print('Welcome to Electrical!')
                    if task1 == 'Fix wiring, ' and task1 in all_tasks:
                        print('This is the fix wiring task, please complete!')
                        time.sleep(1)
                        total_shapes = ['triangle', 'rectangle', 'circle', 'square',
                                        'diamond', 'pentagon', 'hexagon', 'octogon', 'decagon', 'septagon']
                        for i in range(1, 5):
                            shapes = random.choice(total_shapes)
                            total_shapes.remove(shapes)
                            sha = list(shapes)
                            random.shuffle(sha)
                            result = ''.join(sha)
                            swipe = None
                            while swipe == None or swipe != shapes:
                                for i in sha:
                                    print(i, end='')
                                swipe = input("\n")

                        alltasks += 1
                        del_task(all_tasks, task1)
                        print('Task complete!')

                    if upload == 'Elec.':
                        time.sleep(2)
                        print('This is the Uploading Data task.')
                        print('')
                        print('Please wait!')
                        xt = 17
                        while xt != 119:
                            print('')
                            if xt == 112:
                                xt = xt - 12
                            import time
                            print(xt, "% ...")
                            xt = xt + 19
                            time.sleep(2)
                        alltasks += 1
                        print('Task Complete')

                    if task4 == 'Divert power, ' and task4 in all_tasks:
                        answer_for_diversion = None
                        print('This is the divert power task.')
                        Div = ['Admin', 'Reactor', 'Nav.',
                            'Weapons', 'Med bay', 'Engines']
                        Div_power = random.choice(Div)
                        while Div_power != answer_for_diversion:
                            answer_for_diversion = input('Divert power to: ')
                            if answer_for_diversion != Div_power:
                                print("Try again.")
                            else:
                                del_task(all_tasks, task4)
                                break

                        time.sleep(1)

                        print('You can now accept diverted power at', Div_power)

                    elif task1 != "Fix wiring, " or task4 != 'Divert power, ':
                        print('You have no tasks here')

                if loc == 'Reactor':
                    if task2 == 'Start reactor, ' and task2 in all_tasks:
                        while True:
                            req = 0
                            all_answer = ''
                            print('Please start the reactor by typing the following numbers')
                            for i in range(5):
                                answer = str(random.randint(1, 9))
                                all_answer += answer
                                print(all_answer, end='\r')
                                time.sleep(.7)
                                user_answer = input('Type: ')
                                if user_answer != all_answer:
                                    req = 1
                                    break
                            if req == 1:
                                continue
                            else:
                                del_task(all_tasks, task2)
                                alltasks += 1
                                print('Task complete!')
                                break

                    if task3 == 'Unlock manifolds, ' and task3 in all_tasks:
                        results = []
                        user_answers = []
                        for i in range(1, 7):
                            results.append(str(randox(1, 100)))
                        random.shuffle(results)
                        print("Order from least to greatest: ")
                        for result in results:
                            print(result, end=', ')
                        computer_answer = sorted(results)
                        for i in range(len(results)):
                            answer = input(': ')
                            user_answers.append(answer)
                        # print(computer_answer)
                        if computer_answer == user_answers:
                            alltasks += 1
                            del_task(all_tasks, task3)
                            print('Task complete!')
                    else:
                        print()
                        print('You have no more tasks here.')

                if loc == 'Med bay':
                    print('Welcome to Med bay!')
                    if task2 == 'Inspect sample, ' and task2 in all_tasks:
                        list_for_inspection = ['|', '|', '|', '|', RED]

                        print()
                        print('This is the Inspect sample task.')
                        time.sleep(1)
                        input('Press ENTER to start Inspection: ')
                        print()

                        print('Please wait')
                        print()

                        print('ETA (0)', end='\r')
                        time.sleep(1)

                        for i in range(60, 1, -1):
                            print('ETA ({}) '.format(i), end='\r')
                            time.sleep(1)

                        print('Which one does not belong?')
                        print()

                        random.shuffle(list_for_inspection)
                        for index, item in enumerate(list_for_inspection):
                            if item == '\u001b[31m':
                                print('{}: '.format(index + 1), end='')
                                answer = str(index + 1)
                                colour_print('|', item)
                            else:
                                print('{}: '.format(index + 1), end='')
                                colour_print(item, BLUE)

                        odd_tube = input()
                        while odd_tube != answer:
                            print()
                            print('Try again!')
                            odd_tube = input()

                        del_task(all_tasks, task2)
                        alltasks += 1
                        print('Task complete!')

                    if task4 == 'Submit scan, ' and task4 in all_tasks:
                        print('This is the submit scan task.')
                        blood_types = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
                        user_blood_type = random.choice(blood_types)

                        Height = ['3\' 6"', '3\' 4"', '3\' 8"', '3\' 5"']
                        user_height = random.choice(Height)

                        Colour = [RED, BLUE, YELLOW, MAGENTA, CYAN, GREEN]
                        user_colour = random.choice(Colour)

                        Colour_Id = ['REDP1', 'BLUP1', 'YELP2',
                                    'MAGP6', 'CYAP3', 'GREENP0']

                        user_weight = '92LB'

                        if user_colour == RED:
                            colour = 'Red'
                            user_colour_id = Colour_Id[0]
                        if user_colour == YELLOW:
                            colour = 'Yellow'
                            user_colour_id = Colour_Id[2]
                        if user_colour == BLUE:
                            colour = 'Blue'
                            user_colour_id = Colour_Id[1]
                        if user_colour == MAGENTA:
                            colour = 'Magenta'
                            user_colour_id = Colour_Id[3]
                        if user_colour == CYAN:
                            colour = 'Cyan'
                            user_colour_id = Colour_Id[4]
                        if user_colour == GREEN:
                            colour = 'Green'
                            user_colour_id = Colour_Id[5]

                        time.sleep(2)
                        print(f'ID: {user_colour_id}')
                        time.sleep(2)
                        print('HT: {}'.format(user_height))
                        time.sleep(2)
                        print('WT: {}'.format(user_weight))
                        time.sleep(2)
                        colorama.init()
                        print('C: ', end='')
                        colour_print('{}'.format(colour), user_colour)
                        colorama.deinit()
                        time.sleep(2)
                        print('BT: {}'.format(user_blood_type))

                        id_renew = randox(1, 100)
                        if id_renew > 75:
                            print('Please get your ID: {} renewed at Administration.'.format(
                                user_colour_id))
                            renew_id += 1
                            del_task(all_tasks, task4)
                        else:
                            del_task(all_tasks, task4)
                            alltasks += 1
                            print('Task complete!')

                    else:
                        print('You have no more tasks here')

                if loc == 'Engines':
                    print('Welcome to engines!')
                    time.sleep(2)
                    if task2 == 'Fuel engines, ' and task2 in all_tasks:
                        engine_is_fueled = 0
                        print('This is the fuel engines task!')
                        time.sleep(1)
                        engine_type = ['Upper engine', 'Lower engine']
                        # for item in engine_type:
                        for item in engine_type:
                            if engine_is_fueled == 0:
                                print('Please obtain fuel from Storage.')
                                time.sleep(1)
                            else:
                                print('Please obtain more fuel from Storage.')
                                time.sleep(1)
                            print()
                            loc = input(
                                "Where would you like to go? Admin, Storage, 02, Reactor, Nav., Weapons, Med bay, Elec. or Engines: ")

                            if loc == 'Storage':
                                if engine_is_fueled == 0:
                                    print('Welcome to Storage')
                                    time.sleep(1)
                                else:
                                    print('Welcome back to storage')
                                if task2 == 'Fuel engines, ':
                                    user_input = input("Please enter 'Fuel engines': ")
                                    while user_input != 'Fuel engines':
                                        print()
                                        user_input = input("Please enter 'Fuel engines': ")
                                    if user_input == 'Fuel engines':
                                        xt = 20
                                        while xt != 117:
                                            print('')
                                            if xt == 105:
                                                xt = xt - 5
                                            import time
                                            print(xt, "% ...", end='\r')
                                            time.sleep(1)
                                            print('          ', end='\r')
                                            xt = xt + 17
                                        engine_is_fueled += 1
                                        print('Retrun to engines to fuel {}'.format(item))
                                        time.sleep(2)

                                        print()
                                        loc = input(
                                            "Where would you like to go? Admin, Storage, 02, Reactor, Nav., Weapons, Med bay, Elec. or Engines: ")

                            if loc == 'Engines':
                                print('Fueling {}'.format(item))
                                time.sleep(3)

                        del_task(all_tasks, task2)
                        print('Task complete!')
                        alltasks += 1 

                if loc == 'Storage':
                    if task2 == 'Fuel engines, ' and task2 in all_tasks:
                        print('Go to engines for your task!')
                    else:
                        print('You have no tasks here')
                        
                if loc == 'Nav.':
                    pass
            print('Finished')

        if game_type == "2":
            multiplayer = input("Would you like to play 2 player? ")
            print()
            while multiplayer != "yes" and multiplayer != "no":
                print("Invalid operation. Please try again!")
                multiplayer = input("Would you like to play multiplayer? ")
                print()
            if multiplayer == "no":
                            
                level = input("What level would you like to play ? 1, 2 or 3? ")
                print()
                
                if level == "3":
                    rules()
                    Fighter_planes = 10  # fighter planes
                    regeneration = Fighter_planes/2
                    ammo = Fighter_planes
                    print("Level {}, {} fighter planes and {} ammo".format(level, Fighter_planes, ammo))
                    print()
                    
                    while ammo > 0:
                        shoot = input("Press enter to dodge or press 1 to shoot. ")
                        if shoot > "0":
                            ammo = ammo - 1
                            chance = randox(0, 5)
                            if chance > 1:
                                Fighter_planes -= 1
                                ammochance = randox(0, 5)
                                if ammochance > 4:
                                    ammo += 1
                                hello = randox(200, 250)
                                Score += hello
                                print('hit')
                            else:
                                print('miss')
                                
                            value = randox(1, 3)
                            print(Fighter_planes, "fighter planes remain.")
                            if value > 2:
                                health = health - 1
                            print(health, "lives")
                            print(ammo, "ammo left.")

                            
                            if Fighter_planes < 1:
                                break
                            if health < 1:
                                break
                        else:
                            if regeneration > 0:
                                
                                if health < 2:
                                    regeneration -= 1
                                    lifeadd = randox(0, 5)
                                    if lifeadd > 2:
                                        health = health + 1
                                        print()
                                        print("You regained 1 health.")
                                    else:
                                        print()
                                        print("You failed to repair your ship.")
                                        print()
                                        
                            print(Fighter_planes, "fighter planes remain.")
                            print(health, "lives")
                            print(ammo, "ammo left.")
                            print()
                            
                            
                            
                if level == "2": 
                    rules()
                    Fighter_planes = 8 
                    regeneration = Fighter_planes/2
                    ammo = Fighter_planes
                    print("Level {}, {} fighter planes and {} ammo".format(level, Fighter_planes, ammo))
                    print()
                    
                    while ammo > 0:
                        shoot = input("Press enter to dodge or press 1 to shoot. ")
                        if shoot > "0":
                            ammo = ammo - 1
                            chance = randox(0, 50)
                            if chance > 5:
                                Fighter_planes -= 1
                                ammochance = randox(0, 5)
                                if ammochance > 3:
                                    ammo += 1
                                hello = randox(175, 225)
                                Score += hello
                                print('hit')
                            else:
                                print('miss')
                                
                            value = randox(1, 3)
                            print(Fighter_planes, "fighter planes remain.")
                            if value >= 2:
                                health = health - 1
                            print(health, "lives")
                            print(ammo, "ammo left.")

                            
                            if Fighter_planes < 1:
                                break
                            if health < 1:
                                break
                        else:
                            if regeneration > 0:
                                
                                if health < 2:
                                    regeneration -= 1
                                    lifeadd = randox(0, 50)
                                    if lifeadd > 15:
                                        health = health + 1
                                        print()
                                        print("You regained 1 health.")
                                    else:
                                        print()
                                        print("You failed to repair your ship.")
                                        print()
                                        
                            print(Fighter_planes, "fighter planes remain.")
                            print(health, "lives")
                            print(ammo, "ammo left.")
                            print()
                            
                            
                if level == "1":
                    rules()
                    Fighter_planes = 6 
                    regeneration = Fighter_planes/2
                    ammo = Fighter_planes
                    print("Level {}, {} fighter planes and {} ammo".format(level, Fighter_planes, ammo))
                    print()
                    
                    while ammo > 0:
                        shoot = input("Press enter to dodge or press 1 to shoot. ")
                        if shoot > "0":
                            ammo = ammo - 1
                            chance = randox(0, 500)
                            if chance > 25:
                                Fighter_planes -= 1
                                ammochance = randox(0, 1)
                                if ammochance > 0:
                                    ammo = ammo + 1
                                hello = randox(150, 200)
                                Score += hello
                                print('hit')
                            else:
                                print('miss')
                                
                            value = randox(1, 3)
                            print(Fighter_planes, "fighter planes remain.")
                            if value == 1:
                                health = health - 1
                            print(health, "lives")
                            print(ammo, "ammo left.")

                            
                            if Fighter_planes < 1:
                                break
                            if health < 1:
                                break
                        else:
                            if regeneration > 0:
                                
                                if health < 2:
                                    regeneration -= 1
                                    lifeadd = randox(0, 50)
                                    if lifeadd > 5:
                                        health = health + 1
                                        print()
                                        print("You regained 1 health.")
                                    else:
                                        print()
                                        print("You failed to repair your ship.")
                                        print()
                                        
                            print(Fighter_planes, "fighter planes remain.")
                            print(health, "lives")
                            print(ammo, "ammo left.")
                            print()
                            
                endgame(Score, ammo, Fighter_planes)
                

                
            # multiplayer
            if multiplayer == "yes":
                
                while P1ammo > 0:
                    print("P1's turn")
                    shoot = input("Press enter to dodge or press 1 to shoot. ")
                    if shoot > "0":
                        P1ammo -= 1
                        # shooting
                        chance = randox(0, 5)
                        if chance > 1:
                            P2health -= 1
                            # chance of regaining ammo
                            P1ammochance = randox(0, 1)
                            if P1ammochance > 0:
                                P1ammo += 1
                            # score multiplyer
                            P1scoreinc = randox(150, 200)
                            Score += P1scoreinc
                            print('hit')
                        else:
                            print('miss')

                        print("P2 has", P2health, "lives left")
                        print()
                        print("You have", P1health, "lives")
                        print("You have", P1ammo, "ammo left.")
                        print()
                        if P2health < 1:
                            break

                    else:
                        if drango1 > 0:
                            drango1 -= 1
                            if P1health < 3:
                                lifeadd1 = randox(0, 50)
                                if lifeadd1 > 5:
                                    P1health += 1
                                    print()
                                    print("You healed 1 health")
                                    print("P2 has", P2health, "lives left")
                                    print(P1health, "lives")
                                    print(P1ammo, "ammo left.")
                                    print()
                                else:
                                    print()
                                    print("You failed to repair your plane.")
                                    print("P2 has", P2health, "lives left")
                                    print(P1health, "lives")
                                    print(P1ammo, "ammo left.")
                                    print()

                    print("P2's turn")
                    shootc = input("Press enter to dodge or press 1 to shoot. ")
                    if shootc > "0":
                        P2ammo -= 1
                        # shooting opponent:
                        chance2 = randox(0, 5)
                        if chance2 > 1:
                            P1health -= 1
                            # chance of regaining ammo
                            P2ammochance = randox(0, 1)
                            if P2ammochance > 0:
                                P2ammo += 1
                            # score multiplyer
                            P2scoreinc = randox(150, 200)
                            Guest_score += P2scoreinc
                            print('hit')
                        else:
                            print('miss')

                        print("P1 has", P1health, "lives left")
                        print("You have", P2health, "lives left")
                        print("You have", P2ammo, "ammo left.")
                        print()
                        if P1health < 1:
                            break
                    else:
                        if drango2 > 0:
                            drango2 -= 1
                            if P2health < 3:
                                lifeadd2 = randox(0, 50)
                                if lifeadd2 > 5:
                                    P2health += 1
                                    print()
                                    print("You healed 1 health")
                                    print("P1 has", P1health, "lives left")
                                    print(P2health, "lives")
                                    print(P2ammo, "ammo left.")
                                    print()
                                else:
                                    print()
                                    print("You failed to repair your plane.")
                                    print("P1 has", P1health, "lives left")
                                    print(P2health, "lives")
                                    print(P2ammo, "ammo left.")
                                    print()

                if P1ammo > 0:
                    if P1health > 0:
                        print("P1 wins with", Score, "score. Great job!")
                        print("P2 loses with", Guest_score, "score. Nice try")
                    else:
                        print("P2 wins with", Guest_score, "score. Great job!")
                        print("P1 loses with", Score, "score. Nice try")
                else:
                    if P2health > 0:
                        print("P2 wins with", Guest_score, "score. Great job!")
                        print("P1 loses with", Score, "score. Nice try")
                    else:
                        print("P1 wins with", Score, "score. Great job!")
                        print("P2 loses with", Guest_score, "score. Nice try")
                        
                        
        if game_type == '1':
            words = ['rainbow', 'computer', 'science', 'programming', 
            'python', 'mathematics', 'player', 'condition', 
            'reverse', 'water', 'board', 'geeks', 'peanut', 'bunny',
            'atmosphere', 'care', 'flavour', 'master', 'catalogue'] 
            word = random.choice(words)
            
            print("Guess the characters")
            
            guesses = ''
            
            turns = 10
            
            while turns > 0:
                Score = 0
                failed = 0

                for char in word: 
                    if char in guesses: 
                        print(char, end='')
                        Score += random.randint(100, 150)
                        
                    else: 
                        print("_ ",end='')
                        failed += 1
                        
            
                if failed == 0:
                    print("\nYou Win") 
                    
                    print("The word is:", word) 
                    break
                
                guess = input("\nGuess a character:")
                
                guesses += guess 
                
                if guess not in word:
                    turns -= 1
                    print("Wrong")
                    print("You have", + turns, 'more guesses')
                    
                    if turns == 0:
                        print("\nYou Lose")     
                           
    if question == "no":
        e = "Well too bad, Good day to you!"
        print(e)    
    break


                        
with open(f'{username}.txt', 'r') as accountn:
    lines = accountn.readlines()    
                    
for index, line_high in enumerate(lines):
    line_high = line_high.rstrip()
    lines[index] = line_high
      

    if line_high.isnumeric():     
        if Score > int(line_high):
            user_account_for = username, password, Score
            with open(f'{username}.txt', 'w') as accounted:
                for item in user_account_for:
                    print(item, file=accounted)
        break
else:
    with open(f'{username}.txt', 'a') as accounted:
        accounted.write(f"{Score}")

final_in = input()
if final_in == 'h':
    with open(f'{username}.txt', 'r') as my_acount:
        for line in my_acount:
            print(line.strip())
