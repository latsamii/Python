# Latsami Luanglaj
# Program 6
# COP 2500
# 10/20/23

import turtle

# Defines function as trampoline to draw in turtle with a position and radius taken from user
def trampoline(x, y, radius):
    turtle.setheading(0)
               
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)

# Defines function as weightMachine to draw in turtle with a position, length, and width taken from user
def weightMachine(x, y, length, width):
    turtle.setheading(0)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)

# Defines function as pullupRack to draw in turtle with a position and a for loop that draws a pentagon from the length taken from user
def pullupRack(x, y, length):
    turtle.setheading(0)
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(5):
        turtle.forward(length)
        turtle.right(72)

def main():
    print("Let's place the new fitness trampoline!")

# Takes the x, y, and radius inputs from the user to then call trampoline and use the user inputs for the x, y, and radius to draw trampoline
    x = int(input("What is the X coordinate?\n"))
    y = int(input("What is the Y coordinate?\n"))
    radius = int(input("What is the radius?\n"))
    trampoline(x, y ,radius)

    print("\nLet's place the weight machine!")

# Takes the x, y, length, and width from the user to call weightMachine and use the user inputs for the x, y, length, and width to draw weightMachine
    x = int(input("What is the X coordinate?\n"))
    y = int(input("What is the Y coordinate?\n"))
    length = int(input("How long is it?\n"))
    width = int(input("How wide is it?\n"))
    weightMachine(x, y, length, width)

    print("\nLet's place the new pull-up rack!")

# Takes the x, y, and length from the user inputs to then call pullupRack and use the user inputs for the x, y, and length to draw pullupRack
    x = int(input("What is the X coordinate?\n"))
    y = int(input("What is the Y coordinate?\n"))
    length = int(input("How long is it?\n"))
    pullupRack(x, y, length)

main()
               
               
    
    
    

            
    


