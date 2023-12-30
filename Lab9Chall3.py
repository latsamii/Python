# Latsami Luanglaj
# Lab 9 Challenge 3
# COP 2500
# 11/05/23

# Function to count for every element in grade_list to check how many times the element rises
# If true, it will add one to count
def grade_up(grade_list):
    
    count = 0
    
    for i in range(len(grade_list)-1):
        if(grade_list[i] < grade_list[i + 1]):
            count += 1
    return count

# Function that makes an empty list, and then looks at every element in grade_up which will then add itself to better_grades
def evaluate_grades(grades):
    
    better_grades = []
    
    for i in range(len(grades)):
        value = grade_up(grades[i])
        better_grades.append(value)
    return better_grades

# Main function that gives a 2D list, and will call evaluate_grades and have the variable set to it as grades_raise
# Prints out grade_raise
def main():
    grades = [ [95, 92, 93, 96, 92],
             [100, 100],
             [70, 80, 90],
             [95, 85, 75, 70] ]
    
    grade_raise = evaluate_grades(grades)
    print(grade_raise)
    
main()
