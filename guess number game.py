import random

target = random.randint(1, 5)

while True:
    userchoice = (input("Guess a number between 1 and 5 or Quit(Q): "))
    if(userchoice=="Q"):
        break
       
    userchoice= int(userchoice)
  
    if(userchoice == target):
        print("You guessed it right!")
        break
    elif(userchoice < target):
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

print("------GAME OVER------")