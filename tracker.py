# Latsami Luanglaj
# Program 9
# COP 2500
# 11/17/23

# Function named set_goals to ask user for goal category and value and then adds each to dictionary called goals
def set_goals(goals):
    print("Set your goals for the week!")

    for i in range(3):
        category = input("Enter a category for your goal:\n")
        target_goal = int(input("Enter your target for " + str(category) + ":\n"))

        goals[category] = target_goal
        
    return goals

# load_data function where user enters category and value corresponding
def load_data():
    
    data = {}
    goal_path = 0

    print("Enter you data with the category and measurement.")
    print("Type 'done' when done for today.")

    while(goal_path != "done"):
        goal_path = input("Enter category:\n")
        if(goal_path == "done"):
            return data
        value = int(input("Enter value:\n"))

# If a value is being added to the same category if previously added before, then will ask if the new value is adding or replacing old value              
        if(goal_path in data):
            print("You have a value for", goal_path)
            choice = int(input("Do you want to (1) Add to Steps, or (2) Replace Steps?\n"))
            if(choice == 1):
                data[goal_path] += value
            if(choice == 2):
                data[goal_path] = value
        else:
            data[goal_path] = value
    
    return data

# compare_data function where will use keys to go through each dictionary and determine if completed is greater than equal to daily goal 
def compare_data(start_goals, daily_goals, goals_achieve):
    
    common_keys = start_goals.keys() & daily_goals.keys()

    for key in common_keys:
        target_goals = start_goals.get(key)
        completed_goals = daily_goals.get(key)

# checks if the daily inputs are greater than or equal to the goals
        if(completed_goals >= target_goals):
            goals_achieve += 1

# If all three goals are achieved them function will return 1         
    if(goals_achieve == 3):
        return 1
# Else if all three goals were not achieved the function will return 0
    elif(goals_achieve != 3):
        return 0
                  
    return goals_achieve
    
def main():
# Creates empty dictionary called goals
    goals = {}

    goals_achieve = 0
    data = 0
    all_goals = 0

    start_goal = set_goals(goals)
    
# Loops through list called days 
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
# For loop that loops 7 times going through the functions load_data
    for i in range(7):
        if(i == 4):
            print("\nIt's Friday - Happy Friday!")
            daily_goals = load_data()
        else:
            print("\nIt's", days[i])
            daily_goals = load_data()
            
# Calls from goals_achieve to count how many times the user gets all three goals                      
        goals_achieve = compare_data(start_goal, daily_goals, goals_achieve)
        
# If goals_achieve was returned as 1 from the function it will add 1 to all_goals 
        if(goals_achieve == 1):
            all_goals += 1
        
    print("\nYou hit your goals", all_goals, "times this week!")
            
main()
