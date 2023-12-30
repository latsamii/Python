# Latsami Luanglaj
# Lab 4 Challenge 3
# COP 2500
# 09/24/23

# Puts count at 1 since count at default starts at 0
count = 1
wins = 0

# Prints game number and asks for the game score
print("Game #", count, sep = "")
UCF = int(input("What did UCF score: "))
opponent = int(input("What did the opponent score: "))

# While loop where if UCF score is greater than the opponents the loop will continue with the with 1 being added to the count everytime
while(UCF > opponent):
    count += 1
    print("Game #", count, sep = "")
    UCF = int(input("What did UCF score: "))
    opponent = int(input("What did the opponent score: "))
    wins += 1

# If statement where if UCF scores less than the opponent that the while loop stops and the count subtracts 1 with the 
    if(UCF < opponent):
        print("The season is over.")
        print("UCF won", wins,"games.")
        
   
                    

        
    
