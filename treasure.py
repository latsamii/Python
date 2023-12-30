# Latsami Luanglaj
# Lab 7 Challenge 3
# COP 2500
# 10/22/23

# Defines function with the list made in main as the variable and sums the values together
def calc_total(list):
    total = 0
    for i in list:
        total += i
    return total
               
def main():
# Creates a list 
    list = []

# Asks the user how many treasures they would like to find saves as an integer named treasure
    treasure = int(input("How many treasures would you like to find?\n"))

# Sets totalTreasure as 0
    totalTreasure = 0

# For loop in the range of the integer set by user to ask how much each treasure found is, while also adding each value to the list
    for t in range(treasure):
        total = float(input("How much is treasure #" + str(t+1) + " worth?\n"))
        list.append(total)

# Adds the values inputted by the user to totalTreasure, summing the amount of money found by user
        totalTreasure += total

# If statement  for if calc_total(list) is greater than or equal to $1500 then it prints corresponding statement        
    if((calc_total(list) >= 1500)):
        print("You have enough to pay for the next semester! Yay!")
        
# Else statement for if value is not true then it will print corresponding statement
    else:
        print("You do not have enough to pay for next semester.")

main()
 

                
    
    
