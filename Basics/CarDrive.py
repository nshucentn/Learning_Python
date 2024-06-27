command = ""
while True:
    command = input("> ").lower
    if command == "start" :
        print("Car is started...")
    elif command == "Stop" :
        print("Car is stopped...")
    elif command == "help" :
        print('''
              start - to start the car
              stop - to stop the car
              ext - to exit
              ''')
else :
    print("Sorry, I don't understand")
        
        
        
    
    