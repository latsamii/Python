# Latsami Luanglaj
# Lab 3 Challenge 3
# COP 2500
# 09/16/23

import random
import math

# Randomly finds two numbers between -100 and 100
peteyX=random.randint(-100, 100)
peteyY=random.randint(-100, 100)
# Prints two random numbers from the random as X and Y
print("Petey is located at (",peteyX, ",",peteyY, ")")
# Asks user for an X and Y coordinate
xCoordinate=int(input("What is your X coordinate?\n"))
yCoordinate=int(input("What is your Y coordinate?\n"))

# Calculates distance between points from randomInt and points from user
p=[peteyX, peteyY]
q=[xCoordinate, yCoordinate]
peteyDistance=(math.dist(p,q))

# If statement for if the distance calculated is less or greater than 50, to print statement according to so
if(peteyDistance>50):
    print("No Petey in sight.")
elif(peteyDistance<=50):
    print("Oh no! Petey is near!")


