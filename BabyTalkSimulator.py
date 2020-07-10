#import random as rand
from random import choice
questions = ["Why is the sky blue?: ","Why is water wet?: ", "Why is the earth round?: "]

#answer = input(questions[rand.randint(0,2)]).strip().capitalize() #this is one way
answer = input(choice(questions)).strip().capitalize()
while (answer != "Just because!"):
    answer = input("Why?: ").strip().capitalize()

print("Oh..Okay")