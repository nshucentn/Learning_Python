command = ""
car_started = False

while True:
    command = input("> ").lower()
    if command == "start" :
        if car_started :
            print("The car is already started")
        else :
            car_started = True
            print("Car is started...")
    elif command == "stop" :
        if not car_started :
            print("Car is already stopped..")
        else :
            car_started = False
            print("Car is stopped...")
    elif command == "help" :
        print('''
              start - to start the car
              stop - to stop the car
              ext - to exit
              ''')
    elif command == "quit":
        break
    else :
        print("Sorry, I don't understand")
        
        
        
    
    