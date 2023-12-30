# Latsami Luanglaj
# Program 5
# COP 2500
# 10/14/23

def main():

    # Asks user for an int input on how many workouts done
    workouts = int(input("How many worksouts do you have data for?\n"))
    
    # Sets repsTotal to zero
    repsTotal = 0
    
    # For loop where will repeat from int inputted from workouts
    for w in range(workouts):

        # Asks user for int input on how many sets completed in workout
        sets = int(input("How many sets were completed in workout #" + str(w+1) + "?\n"))

        # For loop to repeat from in inputted from sets
        for r in range(sets):

            # Asks user for int input on how many reps from set inputted
            reps = int(input("How many repetitions in set #" + str(r+1) + "?\n"))

            # Adds reps inputted to total repetitons to later be used to find the average
            repsTotal += reps

            # Finds the average of repetitions in each set
            avgReps = repsTotal / sets

        # Prints the average repetitions of the set, with only three decimal points showing            
        print("Workout #" + str(w+1) + ": The average number of repetitions was %.3f\n" %(avgReps))

        # Puts total repetitions back to zero to not keep total repetitions from previous sets
        repsTotal = 0                   
main()        
