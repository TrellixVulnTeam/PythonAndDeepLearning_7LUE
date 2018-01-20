#Guess Game
from random import randint

randNum = randint(0,9)  #Generate random integer between 0 and 9

print("Suppose the digit generated by program is ",randNum)

guessString = input('Guess the digit: ')    #User enters guessed value
guessNumber = int(guessString)

#if random number matches with guessed value
if guessNumber == randNum:
    print("Your answer is PERFECT!! Congratulations!!")

#if random number is greater than guessed value
elif guessNumber < randNum:
    print("Your answer is low than required")

#if random number is less than guessed value
else:
    print("Your answer is high than required")