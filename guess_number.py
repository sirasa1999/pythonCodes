#Guess the number game

import random

while True:
    inputt= True
    while inputt:
        num=input("Enter the number range: ")
        if num.isdigit():
            print("Let's Start!!!")
            num=int(num)
            inputt=False
        else:
            print("Invalid input, please type again.")

    gen=random.randint(1,num)
    guess=None
    count=1
    while guess!=gen:
        guess=input("Enter a number between 1 and " + str(num) + ": ")
        if guess.isdigit():
            guess=int(guess)
        if guess==gen:
            print("You've guess the right numer.CONGRATULATIONS!!!")
        else:
            print("Sorry,please enter your next guess.")
            count+=1
    print("You have completed in ",count, "guesses.")

