

"""VARIABLES"""
# Creates a variable with a string "Frankfurter"
title = "Frankfurter"

# Creates a variable with an integer 80
years = 80

# Creates a variable with the boolean value of True
expert_status = True

# How to know what kind of variable you have
type(expert_status) # or years, or title

# Convert your variable into another one
str(years) # int() list()


# Prints a statement adding the variable
print("Nick is a professional " + title)

# Convert the integer years into a string and prints
print("He has been coding for " + str(years) + " years")

# Converts a boolean into a string and prints
print("Expert status: " + str(expert_status))


# An f-string accepts all data types without conversion. See more examples: https://realpython.com/python-f-strings/
print(f"Expert status: {expert_status} ")




"""LISTS - think of them as one-dimensional arrays similar to an excel column"""
# Create a variable and set it as an List
myList = ["Jacob", 25, "Ahmed", 80]
print(myList)

# Adds an element onto the end of a List
myList.append("Matt")
print(myList)

# Returns the index of the first object with a matching value
print(myList.index("Matt"))

# Changes a specified element within an List at the given index
myList[3] = 85
print(myList)

# Returns the length of the List
print(len(myList))

# Removes a specified object from an List
myList.remove("Matt")
print(myList)

# Removes the object at the index specified
myList.pop(0)
myList.pop(0)
print(myList)


# Creates a tuple, a sequence of immutable Python objects that cannot be changed See more: https://www.quora.com/What-advantages-do-tuples-have-over-lists
myTuple = ('Python', 100, 'VBA', False)
print(myTuple)





"""DICTIONARIES - think of these as two excel columns"""

# Unlike lists, dictionaries store information in pairs
# ---------------------------------------------------------------

# A list of actors
actors = ["Tom Cruise",
          "Angelina Jolie",
          "Kristen Stewart",
          "Denzel Washington"]

# A dictionary of an actor
actor = {"name": "Tom Cruise"}
print(f'{actor["name"]}')

# ---------------------------------------------------------------

# A dictionary can contain multiple pairs of information
actress = {
    "name": "Angelina Jolie",
    "genre": "Action",
    "nationality": "United States"
}

# ---------------------------------------------------------------

# A dictionary can contain multiple types of information
another_actor = {
    "name": "Sylvester Stallone",
    "age": 62,
    "married": True,
    "best movies": [
        "Rocky",
        "Rocky 2",
        "Rocky 3"]}
print(f'{another_actor["name"]} was in {another_actor["best movies"][0]}')
# ---------------------------------------------------------------

# A dictionary can even contain another dictionary
film = {
    "title": "Interstellar",
    "revenues": {
        "United States": 360,
        "China": 250,
        "United Kingdom": 73
    }
}
print(f'{film["title"]} made {film["revenues"]["United States"]}'" in the US.")
# ---------------------------------------------------------------




"""CONDITIONALS - IF STATEMENTS"""
x = 1
y = 10

# Checks if one value is equal to another
if x == 1:
    print("x is equal to 1")

# Checks if one value is NOT equal to another
if y != 1:
    print("y is not equal to 1")

# Checks if one value is less than another
if x < y:
    print("x is less than y")

# Checks if one value is greater than another
if y > x:
    print("y is greater than x")

# Checks if a value is less than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")

# Checks for two conditions to be met using "and"
if x == 1 and y == 10:
    print("Both values returned true")

# Checks if either of two conditions is met
if x < 45 or y < 5:
    print("One or more of the statements were true")

# Nested if statements
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")
        
# Sometimes you may have too many if statements. Try using a dictionary        
# Example of a switch statement with dictionaries
choices = {'a': 1, 'b': 2, 'c': 3}
result = choices.get('a', 'default')
print(result)


        
""" LOOPS """     


# Loop through a range of numbers (0 through 4)
for x in range(5):
    print(x)

print("-----------------------------------------")

# Loop through a range of numbers (2 through 6 - yes 6! Up to, but not including, 7)
for x in range(2, 7):
    print(x)

print("----------------------------------------")

# Iterate through letters in a string
word = "Peace"
for letters in word:
    print(letters)

print("----------------------------------------")

# Iterate through a list
zoo = ["cow", "dog", "bee", "zebra"]
for animal in zoo:
    print(animal)

print("----------------------------------------")

# Loop while a condition is being met
run = "y"

while run == "y":
    print("Hi!")
    run = input("To run again. Enter 'y'")
    
# While loops are best used when an exogenous event tells a programm to stop (usually a boolean true or false)
# For example, while the autonomous car is driving, scan the environment, but when the car is not driving, then cancel the while loop of scanning the environment around car
# Another example, while video game is not paused, keep the environment going, but when the player hits pause, then stop (pause is a boolean here (true or false))

# Doing a for loop with while loop is possible, but looks more complicated
i=0
while i<10:
    print(i)
    i=i+1
    



    
""" FUNCTIONS - def <name of function>() """


# Define the function and tell it to print "Hello!" when called
def printHello():
    print(f"Hello!")


# Call the function within the application to ensure the code is run
printHello()
# -------------#


# Functions that take in and use parameters can also be defined
def printName(name):
    print("Hello " + name + "!")


# When calling a function with a parameter, a parameter must be passed into the function
printName("Bob Smith")
# -------------#

# The prime use case for functions is in being able to run the same code for different values
listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listTwo = [11, 12, 13, 14, 15]


def listInformation(simpleList):
    print(f"The values within the list are...")
    for value in simpleList:
        print(value)
    print("The length of this list is... " + str(len(simpleList)))


listInformation(listOne)
listInformation(listTwo)



# Example of our fizzbuzz challenge from previous VBA class in Python, you can see how it's much shorter than VBA's syntax
for i in range(1, 101):
    if(i % 3 == 0 and i % 5 == 0):    # or  if i % 15 == 0: as Kesh suggested last class
        print ('FizzBuzz')
    elif i % 3 == 0:
        print ('Fizz')
    elif i % 5 == 0:
        print ('Buzz')
    else:
        print (str(i))
        

# go over import library 

