Secret_Number = 9
Guess_Count = 0
Guess_Limit = 3

while Guess_Count < Guess_Limit:
    Guess = int(input('Guess :'))
    Guess_Count+=1
    if Guess == Secret_Number :
        print("You've Won")
        break
else :
        print("You've lost")
   
    