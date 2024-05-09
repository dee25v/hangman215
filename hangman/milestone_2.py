# Step 1: Create a list containing the names of your 5 favourite fruits
word_list = ["Apple", "Banana", "Mango", "Orange", "Grape"]

# Step 2: Assign this list to a variable called word_list (already done in Step 1)

#Step 3: Print out the newly created list to the standard output (screen)
print("My favourite fruits are:" , word_list)

import random

# Step 1-3: Create a list containing the names of your 5 favorite fruits
# and randomly select a word from the list
word_list = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
word = random.choice(word_list)

# Step 4: Assign the randomly generated word to a variable called word

# Step 5: Print out word to the standard output
print("Randomly selected word:", word)

# Step 1: Create a list containing the names of your 5 favourite fruits
word_list = ["Apple", "Banana", "Mango", "Orange", "Grape"]

# Step 2: Assign this list to a variable called word_list (already done in Step 1)

#Step 3: Print out the newly created list to the standard output (screen)
print("My favourite fruits are:" , word_list)

# Step 1: Create an if statement that checks if the length of the input is equal to 1
# and the input is alphabetical
import string

while True:
    guess = input("Enter a single letter: ")
    if len(guess) == 1 and guess.isalpha():
        # Step 2: In the body of the if statement, print a message that says "Good guess!"
        print("Good guess!")
        break
    else:
        # Step 3: Create an else block that prints "Oops! That is not a valid input."
        # if the preceding conditions are not met
        print("Oops! That is not a valid input.")

# Meaningful Naming: Use descriptive names for methods and variables to enhance code readability
# For example, create_list_of_website_links() over links() and use for element in web_element_list instead of for i in list

def get_user_input():
    """
    Gets user input and validates that it is a single alphabetical character.
    """
    while True:
        guess = input("Enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Oops! That is not a valid input.")

# Eliminate Code Duplication: Identify repeated code blocks and refactor them into separate methods or functions
# This promotes code reusability and reduces the likelihood of bugs

def print_good_guess_message(guess):
    """
    Prints a message that says "Good guess!" if the user's input is a single alphabetical character.
    """
    print("Good guess!")

# Main program

guess = get_user_input()
print_good_guess_message(guess)
