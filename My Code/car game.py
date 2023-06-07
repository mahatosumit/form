print('''
some important key to play game
type:
"start" to start car
"run" to run car
"quit" to stop car
''')
start_game =""
started = True
running = True
while start_game != "quit":
    start_game = input("Enter arguments to start game:\n")
    if start_game == "start":
        if started:
            print("The car is already started!")
        else:
            print("You started car!")
    elif start_game == "run":
        if running:
            print("The car is already running!")
        else:
            print("the car is running!")


    elif start_game == "stop":
       if start_game != "run":
            print("The car is not running")
       else :
           print("You stopped car!")
    elif start_game == "quit":
        break
    else :
        print("Sorry! You entered wrong argument")