# Latsami Luanglaj
# Problem 4 Heart Rate Monitor
# COP 2500
# 09/29/23

# Makes count for the total recorded heart rates to 0
totaltargetHR = 0

# Asks user for an input of their gender and age
gender = input("Do you want to use the target heart rate for men or women?\n")
age = int(input("How old are you?\n"))

# If statement to see if targeted heart rate should be for men or women
if(gender == "women" or "Women"):
     targetHR = 220 - age
elif(gender == "men" or "Men"):
     targetHR == 226 - age

# Asks user for first input in recorded heart rate adds to totaltargetHR if heart rate is in range
heartRate = int(input("Please enter your recorded heart rates: \n"))
if(heartRate == targetHR):
    totaltargetHR += 1

# Adds 1 to recordedHR since user inputed 1 recorded heart rate    
recordedHR = 1

# While loop for if input by user does not equal -1 the loop will continue, but to also add one to recordedHR which is the total amount of recorded heart rates the user has inputted          
while(heartRate != -1):
    heartRate = int(input())
    recordedHR += 1

# If statement to add one if the recorded heart rate that user inputs is equal to the targetHR for the gender   
    if(heartRate == targetHR):
        totaltargetHR += 1

# If statement to get out of loop if the user inputs -1 and prints amount of times user hit targeted heart rate        
    if(heartRate == -1):
        print("You hit your target heart rate", totaltargetHR, "times out of", recordedHR - 1, end = "")
        print("!")
