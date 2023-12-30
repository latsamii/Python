# Latsami Luanglaj
# Problem 2 BMI
# COP 2500
# 09/15/23

# Taking in height input from user
height=int(input("What is your height in inches?\n"))

# Taking in weight input from user
weight=int(input("What is your weight in pounds?\n"))

# Calculates BMI from users input
BMI=(weight*703)/(height*height)

# Prints BMI with %.2f to only show value with two decimal points
print("Your BMI is calculated at %.2f" %(BMI))
