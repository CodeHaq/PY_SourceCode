import random
import time
from Colour_print import GREEN, RED, BLUE, YELLOW, CYAN, MAGENTA, colour_print
import colorama
from threading import Thread

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


print()
print("Among us, Booting up!")
renew_id = 0
time.sleep(1)
Commontasks = ['Enter ID, ', 'Fix wiring, ', 'Insert keys, ']
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
print()
print("These are your tasks;", task1, task2, task3, task4)
all_tasks = [task1, task2, task3, task4]
upload = None
Div_power = None
while alltasks != 4:
    print()
    loc = input(
        "Where would you like to go? Admin, Storage, 02, Reactor, Nav., Weapons, Med bay, Elec. or Engines: ")
    if loc == "tasks":
        print()
        print("These are your tasks;", task1, task2, task3, task4)
    if loc == "Admin":

        print()
        print('Welcome to Admin')
        time.sleep(1)
        print()
        if task1 == "Enter ID, " and task1 in all_tasks:

            print('This is the Enter ID task, please enter the number given.')
            time.sleep(1)
            print()
            vart = randox(10000, 99999)
            print("You have 6 seconds to complete this task.")
            time.sleep(1.5)
            print(vart)
            print()

            
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
            swipe = int(input())

            if vart == swipe:
                print('Task complete!')
                del_task(all_tasks, task1)

                alltasks += 1
            else:
                print()
                while vart != swipe:
                    vart = randox(10000, 99999)
                    print(vart)
                    swipe = int(input())
                    if vart == swipe:
                        alltasks += 1
                        del all_tasks[0]
                        print(all_tasks)
                        print('Task complete!')
                        break
        
        if task2 == "Upload data, " and task2 in all_tasks:

            time.sleep(2)
            print('This is the Downloading Data task.')
            print()
            print('Please wait!')
            xt = 20
            while xt != 117:
                print()
                if xt == 105:
                    xt = xt - 5
                import time
                print(xt, "% ...")
                xt = xt + 17
                time.sleep(2)
            uploadpoint = ['Elec.', 'Nav.', 'Weapons']
            upload = random.choice(uploadpoint)
            del_task(all_tasks, task2)
            print('Please upload data at', upload)

        if Div_power == 'Admin' and 'Admin' in Div_power:
            while True:
                ac = input('Please accept Diverted power: ')
                ac.casefold()
                if ac == 'accept diverted power':
                    alltasks += 1
                    print('Task Complete!')
                    del_task(list(Div_power), 'Admin')
                    break
                else:
                    print()
                    print('Try again')
                    
                    
        if renew_id == 1:
            print('Please wait while your ID gets renewed')
            time.sleep(1)
            alltasks += 1
            print('ID is renewed')

        else:
            print()
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
            print()
            print('Please wait!')
            xt = 17
            while xt != 119:
                print()
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
        if Div_power == 'Reactor' and 'Reactor' in Div_power:
            while True:
                ac = input('Please accept Diverted power: ')
                ac.casefold()
                if ac == 'accept diverted power':
                    alltasks += 1
                    print('Task Complete!')
                    del_task(list(Div_power), 'Reactor')
                    break
                else:
                    print()
                    print('Try again')
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

            def check():
                for i in range(60, 1, -1):
                    print('ETA ({}) '.format(i), end='\r')
                    time.sleep(1)
                return
            Thread(target=check).start()

            time.sleep(60)            

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
                
                
                
        if Div_power == 'Med bay' and 'Med bay' in Div_power:
            while True:
                ac = input('Please accept Diverted power: ')
                ac.casefold()
                if ac == 'accept diverted power':
                    alltasks += 1
                    print('Task Complete!')
                    del_task(list(Div_power), 'Med bay')
                    break
                else:
                    print()
                    print('Try again')
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
                                print()
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
                            loc = input("Where would you like to go? Admin, Storage, 02, Reactor, Nav., Weapons, Med bay, Elec. or Engines: ")

                if loc == 'Engines':
                    print('Fueling {}'.format(item))
                    time.sleep(3)
                else:
                    break

            del_task(all_tasks, task2)
            print('Task complete!')
            alltasks += 1 
            
            
        if Div_power == 'Engines' and 'Engines' in Div_power:
            while True:
                ac = input('Please accept Diverted power: ')
                ac.casefold()
                if ac == 'accept diverted power':
                    alltasks += 1
                    print('Task Complete!')
                    del_task(list(Div_power), 'Engines')
                    break
                else:
                    print()
                    print('Try again')
                    
                    
    if loc == 'Storage':
        if task2 == 'Fuel engines, ' and task2 in all_tasks:
            print('Go to engines for your task!')
        else:
            print('You have no tasks here')
            
    if loc == 'Nav.':
        if task3 == 'Stabilize steering, ' and task3 in all_tasks:
            latitude = randox(1, 100)
            longtitude = randox(1, 100)
            print(latitude, longtitude)
            





print('Finished')
