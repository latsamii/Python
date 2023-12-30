# Latsami Luanglaj
# Program 7
# COP 2500
# 11/02/23

# Function where it adds the inputs inputted by user to list called ingredients
def load_list(ingredients):
    
    ingredients.append(float(input("How many bananas do you have?\n")))
    ingredients.append(float(input("How many strawberries do you have?\n")))
    ingredients.append(float(input("How many blueberries do you have?\n")))
    ingredients.append(float(input("How many cups of spinach do you have?\n")))
    ingredients.append(float(input("How many avocados do you have?\n")))

# Menu function where it takes the int input by user and returns it
def menu():
    
    print("\nWhat would you like to do?\n")
    print("1 - View Ingredients")
    print("2 - Update Ingredients")
    print("3 - Make a Smoothie")
    print("4 - Quit")
    choice = int(input())

    return choice

# View function where it takes the list from ingredients and shows the amount of each variable from ingredients
def view_list(ingre_list):
    
    print("\nAmount of Ingredients:")
    print("Bananas:", ingre_list[0])
    print("Strawberries:", ingre_list[1])
    print("Blueberries:", ingre_list[2])
    print("Spinach:", ingre_list[3], "cups")
    print("Avocados:", ingre_list[4])

# Function where it overwrites each variable in list with new input by user
def update_list(ingredients):
    
    ingredients[0] = float(input("How many bananas do you have?\n"))
    ingredients[1] = float(input("How many strawberries do you have?\n"))
    ingredients[2] = float(input("How many blueberries do you have?\n"))
    ingredients[3] = float(input("How many cups of spinach do you have?\n"))
    ingredients[4] = float(input("How many avocados do you have?\n"))          

# Function where it asks user to say yes or no if said yes and has correct amount of ingredients it will subtract it from appropriate element in the list, if yes and does not have correct amount it will print statement and add back elements that had correct amounts 
def make_smoothie(ingredients):
    
    bananas=input("Will you use bananas?\n")
    if(bananas == "yes" and ingredients[0] >= 1):
        ingredients[0] -= 1
    elif(bananas == "yes" and ingredients[0] < 1):
        print("\nSorry, this recipe cannot be completed.")
        return
    
    strawberries=input("Will you use strawberries?\n")
    if(strawberries == "yes" and ingredients[1] >= 5):
        ingredients[1] -= 5
    elif(strawberries == "yes" and ingredients[1] < 5):
        print("\nSorry, this recipe cannot be completed.")
        if(bananas == "yes"):
            ingredients[0] += 1
        if(strawberries == "yes"):
            ingredients[1] += 5
        return
    
    blueberries=input("Will you use blueberries?\n")
    if(blueberries == "yes" and ingredients[2] >= 12):
        ingredients[2] -= 12
    elif(blueberries == "yes" and ingredients[2] < 12):
        print("\nSorry, this recipe cannot be completed.")
        if(bananas == "yes"):
            ingredients[0] += 1
        if(strawberries == "yes"):
            ingredients[1] += 5
        return
    
    spinach=input("Will you use spinach?\n")
    if(spinach == "yes" and ingredients[3] >= 1):
        ingredients[3] -= 1
    elif(spinach == "yes" and ingredients[3] < 1):
        print("\nSorry, this recipe cannot be completed.")
        if(bananas == "yes"):
            ingredients[0] += 1
        if(strawberries == "yes"):
            ingredients[1] += 5
        if(blueberries == "yes"):
            ingredients[2] += 12
        return
    
    avocados=input("Will you use avocados?\n")
    if(avocados == "yes" and ingredients[4] >= 0.5):
        ingredients[4] -= 0.5
    elif(avocados == "yes" and ingredients[4] < 0.5):
        print("\nSorry, this recipe cannot be completed.")
        if(bananas == "yes"):
            ingredients[0] += 1
        if(strawberries == "yes"):
            ingredients[1] += 5
        if(blueberries == "yes"):
            ingredients[2] += 12
        if(spinach == "yes"):
            ingredients[3] += 1
        if(avocados == "yes"):
            ingredients[4] += 0.5
        return
    
# drink_score and health_score set to 0
    drink_score = 0
    health_score = 0
    
# If statements for if spinach and avocados are inputted as yes, then will add accordingly to drink and health score
    if(avocados == "yes" and spinach == "yes"):
        drink_score += 0
        health_score += 2
    if(avocados == "yes" and spinach == "no"):
        drink_score += 1
        health_score += 1
    if(avocados == "no" and spinach == "yes"):
        drink_score += 1
        health_score += 1
    if(avocados == "no" and spinach == "no"):
        drink_score += 1
        health_score += 0
        
# If statement for when drink_score is either 0, or 1 it will print out correct statment
    if(drink_score == 0):
        print("\nYour recipe scored a Drink Score of 0. Yuck!")
    if(drink_score == 1):
        print("\nYour recipe scored a Drink Score of 1. It will be delicious!")
        
# If statement for when health_score is either 0, 1, or 2 it will print out correct statement
    if(health_score == 0):
        print("Your recipe scored a Health Score of 0. It probably tastes good though.")
    if(health_score == 1):
        print("Your recipe scored a Health Score of 1. It is good to go!")
    if(health_score == 2):
        print("Your recipe scored a Health Score of 2. It will be super healthy!")
        
# Main function that makes an empty list called smoothie_list and takes from load_list to attain list inputted by user
# Then prints out menu(), where user is then put into while loop where as long as 4 isnt inputted then it will continue
# Main function will take view_list to see smoothie_list, update_list to change smoothie_list, and make_smoothie to make a smoothie and get a drink and health score
def main():
    smoothie_list = []
    load_list(smoothie_list)

    option = menu()

    while(option != 4):
        if(option == 1):
            view_list(smoothie_list)
        if(option == 2):
            update_list(smoothie_list)
        if(option == 3):
            make_smoothie(smoothie_list)

        option = menu()

main()


    
    
