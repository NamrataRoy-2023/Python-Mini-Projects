import random

num = random.randint(0,100)
print("Lets Start!!")
while True:
    userInput=input("Guess the Number or Quit(Q): ")
    
    if(userInput == "Q"):
        break
    
    userInput = int(userInput)
    if(userInput == num):
        print("You WIN!! Hurray!! You Guessed it Correct.")
        break
    elif(userInput < num):
        print("Try to Guess a Larger Number")
        
    elif(userInput > num):
        print("Try to Guess a Smaller Number")
        
    else:
        print("Invalid Input")
print("---GAME OVER---")
print("Lets Start Again")