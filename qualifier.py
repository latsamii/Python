# Latsami Luanglaj
# Program 8
# COP 2500
# 11/07/23

# Function add time, where racer_a and racer
def add_time(racer_a, racer_b):
    
    time = input("Which racer is adding a time?\n")
    if(time == "A"):
        racer_a.append(float(input("What is the time to be added?\n")))
        return menu()
    
    if(time == "B"):
        racer_b.append(float(input("What is the time to be added?\n")))
        return menu()

    if(time != "A" or "B"):
        print("Could not interpret racer. Please use A or B.")
        return menu()
    
def delete_time(racer_a, racer_b):
    
    if( (len(racer_a)) == 0 or (len(racer_b) == 0) ):
        print("At least one racer has no time!")
        return
    
    else:
        del_racer = input("Which racer is deleting a time?\n") 
        if(del_racer == "A"):
            del_type = input("Delete a time or delete a race?\n")
                
            if(del_type == "race"):
                del_race = int(input("Which race should be deleted?\n"))
                racer_a.pop(del_race - 1)
            elif(del_type == "time"):
                del_time = input("Which time should be deleted?\n")
                if del_time in racer_a:
                    racer_a.remove(del_time)
            elif(del_type != "race" or del_type != "time"):
                print("Could not interpret deletion. Please use time or race.")
            return  
        if(del_racer == "B"):
            del_type = input("Delete a time or delete a race?\n")    
            if(del_type == "race"):
                del_race = int(input("Which race should be deleted?\n"))
                racer_b.pop(del_race - 1)
            elif(del_type == "time"):
                del_time = float(input("Which time should be deleted?\n"))
                if del_time in racer_b:
                    racer_b.remove(del_time)
                    
            elif(del_type != "race" or del_type != "time"):
                print("Could not interpret deletion. Please use time or race.")
            return
        
def compare_time(racer_a, racer_b):
    
    if( (len(racer_a)) == 0 or (len(racer_b)) == 0):
        print("At least one racer has no times!")
        return menu()
    
    else:
        print("\nRacer A has data for", len(racer_a), "races.")
        print("Racer B has data for", len(racer_b), "races.")

        if( (len(racer_a)) == (len(racer_b)) ):
            print("\nWe will compare the first", len(racer_a), "races.")
            for i in range(len(racer_a)):
                    racetime_a = racer_a[i]
                    racetime_b = racer_b[i]
                    if(racetime_a > racetime_b):
                        print("Racer B has won race #", i + 1, sep = "")
                    elif(racetime_a < racetime_b):
                        print("Racer A has won race #", i + 1, sep = "")
                    else:
                        print("The racers tie race #", i + 1, sep = "")
                        
        elif( (len(racer_a)) != (len(racer_b)) ):
            
            if( (len(racer_a)) < (len(racer_b)) ):
                print("We will compare the first", len(racer_a), "races.")
                for i in range(len(racer_a)):
                    racetime_a = racer_a[i]
                    racetime_b = racer_b[i]
                    if(racetime_a > racetime_b):
                        print("Racer B has won race #", i + 1, sep = "")
                    elif(racetime_a < racetime_b):
                        print("Racer A has won race #", i + 1, sep = "")
                    else:
                        print("The racers tie race #", i + 1, sep = "")
                        
            elif( (len(racer_a)) > (len(racer_b)) ):
                print("We will compare the first", len(racer_b), "races.")
                for i in range(len(racer_b)):
                    racetime_a = racer_a[i]
                    racetime_b = racer_b[i]
                    if(racetime_a > racetime_b):
                        print("Racer B has won race #", i + 1, sep = "")
                    elif(racetime_a < racetime_b):
                        print("Racer A has won race #", i + 1, sep = "")
                    else:
                        print("The racers tie race #", i + 1, sep = "")

def check_qualifier(racer_a, racer_b, qualifier):
    
    for i in range(len(qualifier)):
        print("Qualifier #", i + 1, sep = "")
        qualifiertime_a = racer_a[i]
        qualifiertime_b = racer_b[i]
        if(qualifiertime_a <= qualifier[i] and qualifiertime_b <= qualifier[i]):
            print("Racer A Qualifies!\nRacer B Qualifies!")
        elif(qualifiertime_a <= qualifier[i]):
            print("Racer A Qualifies!")
        elif(qualifiertime_b <= qualifier[i]):
            print("Racer B Qualifies!")
        else:
            print("Neither racer qualified.")
            
def menu():

    print("\nWhat would you like to do?")
    print("1 - Add a time")
    print("2 - Delete a time")
    print("3 - Compare times")
    print("4 - Check qualifiers")
    print("5 - Quit")
    choice = int(input())

    if(choice > 5 or choice < 1):
        print("That was not a valid option.")
        return menu()

    return choice
           
def main():
    racer_a = []
    racer_b = []
    qualifier = []

    print("Enter Times for Racer A:")
    for i in range(3):
        racer_a.append(float(input("Race #" + str(i+1) + ": ")))
        
    print("\nEnter Times for Racer B:")
    for i in range(3):
        racer_b.append(float(input("Race #" + str(i+1) + ": ")))

    print("\nEnter times for the qualifiers:")
    for i in range(3):
        qualifier.append(float(input("Race #" + str(i+1) + ": ")))

    option = menu()

    while(option != 5):
        if(option == 1):
            add_time(racer_a, racer_b)
        if(option == 2):
            delete_time(racer_a, racer_b)
        if(option == 3):
            compare_time(racer_a, racer_b)
        if(option == 4):
            check_qualifier(racer_a, racer_b, qualifier)

        option = menu()
        
main()
