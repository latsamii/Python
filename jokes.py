# Latsami Luanglaj
# Lab 8 Challenge 3
# COP 2500
# 10/29/23

def joke_splicer(jokes):
# Creates an empty list called joke
    joke = []
# Splits jokes when there is ##
    jokes = jokes.split("##")

# For loop for every value in jokes it will take the white space away and capitalize first letter of each word only   
    for j in jokes:
        clean_jokes = j.strip()
        clean_jokes = clean_jokes.title()
# Adds clean_joke to list joke        
        joke.append(clean_jokes)
        
# Sorts joke list by numerical order        
        joke.sort()

# If statement for if there is an empty string it will remove it
        if(('') in joke):
            joke.remove('')
# Returns joke           
    return(joke)
    

def main():
   j = '''1. WHAT DID THE OCEAN SAY TO THE PIRATE? NOTHING, IT JUST WAVED.##
5. HOW DO PIRATES PREFER TO COMMUNICATE? AYE TO AYE!##
3. WHERE CAN YOU FIND A PIRATE WHO HAS LOST HIS WOODEN LEGS? RIGHT WHERE YE LEFT HIM.##
7. HOW DID THE PIRATE GET HIS JOLLY ROGER SO CHEAP? HE BOUGHT IT ON SAIL.##
2. WHY IS PIRATING SO ADDICTIVE? THEY SAY ONCE YE LOSE YER FIRST HAND, YE GET HOOKED.##
4. HOW MUCH DID THE PIRATE PAY FOR HIS PEG AND HOOK? AN ARM AND A LEG.##
6. HOW DO YOU MAKE A PIRATE FURIOUS? TAKE AWAY THE P.##
       '''
   answer = joke_splicer(j)
   print(answer)

main()
