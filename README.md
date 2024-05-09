# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

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

# Step 1: Create a while loop and set the condition to True.
# Setting the condition to True ensures that the code runs continuously.

while True:

    # Step 2: Ask the user to guess a letter and assign this to a variable called guess.
    guess = input("Guess a letter: ")

    # Step 3: Check that the guess is a single alphabetical character.
    # Hint: You can use Python's isalpha method to check if the guess is alphabetical.
    if len(guess) == 1 and guess.isalpha():

        # Step 4: If the guess passes the checks, break out of the loop.
        break

    # Step 5: If the guess does not pass the checks, then print a message saying
    # "Invalid letter. Please, enter a single alphabetical character."
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# Print a message saying "Good guess!"
print("Good guess!")

# Import the required libraries
import random

# Define a list of words
word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango"]

# Randomly choose a word from the list
secret_word = random.choice(word_list)

# Create a list of underscores with the same length as the secret word
word_so_far = ["_"] * len(secret_word)

# Create a while loop and set the condition to True
while True:

    # Ask the user to guess a letter and assign this to a variable called guess
    guess = input("Guess a letter: ")

    # Check that the guess is a single alphabetical character
    if len(guess) == 1 and guess.isalpha():

        # Check whether the letter guessed by the user is in the secret word
        if guess in secret_word:

            # If the guess is in the word, print a message saying "Good guess! {guess} is in the word."
            print("Good guess! " + guess + " is in the word.")

            # Loop through the word_so_far list
            for i in range(len(word_so_far)):

                # If the guess is in the secret word, replace the underscore with the guess
                if guess == secret_word[i]:
                    word_so_far[i] = guess

            # Print the word_so_far list
            print(" ".join(word_so_far))

            # If the word_so_far list is the same as the secret word, break out of the loop
            if "".join(word_so_far) == secret_word:
                print("Congratulations! You guessed the word " + secret_word + "!")
                break

        # If the guess is not in the word, print a message saying "Sorry, {guess} is not in the word. Try again."
        else:
            print("Sorry, " + guess + " is not in the word. Try again.")

    # If the guess is not a single alphabetical character, print a message saying "Invalid letter. Please, enter a single alphabetical character."
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# Import the required libraries
import random

# Define a list of words
word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango"]

# Randomly choose a word from the list
secret_word = random.choice(word_list)

# Create a list of underscores with the same length as the secret word
word_so_far = ["_"] * len(secret_word)

# Define the check_guess function
def check_guess(guess):

    # Convert the guess into lower case
    guess = guess.lower()

    # Check whether the letter guessed by the user is in the secret word
    if guess in secret_word:

        # If the guess is in the word, print a message saying "Good guess! {guess} is in the word."
        print("Good guess! " + guess + " is in the word.")

        # Loop through the word_so_far list
        for i in range(len(word_so_far)):

            # If the guess is in the secret word, replace the underscore with the guess

# Import the required libraries
import random

# Define a list of words
word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango"]

# Randomly choose a word from the list
secret_word = random.choice(word_list)

# Create a list of underscores with the same length as the secret word
word_so_far = ["_"] * len(secret_word)

# Define the check_guess function
def check_guess(guess):

    # Convert the guess into lower case
    guess = guess.lower()

    # Check whether the letter guessed by the user is in the secret word
    if guess in secret_word:

        # If the guess is in the word, print a message saying "Good guess! {guess} is in the word."
        print("Good guess! " + guess + " is in the word.")

        # Loop through the word_so_far list
        for index in range(len(word_so_far)):

            # If the guess is in the secret word, replace the underscore with the guess
            if guess == secret_word[index]:
                word_so_far[index] = guess

        # Print the word_so_far list
        print(" ".join(word_so_far))

        # If the word_so_far list is the same as the secret word, break out of the loop
        if "".join(word_so_far) == secret_word:
            print("Congratulations! You guessed the word " + secret_word + "!")

    # If the guess is not in the word, print a message saying "Sorry, {guess} is not in the word. Try again."
    else:
        print("Sorry, " + guess + " is not in the word. Try again.")

# Define the ask_for_input function
def ask_for_input():

    # Create a while loop and set the condition to True
    while True:

        # Ask the user to guess a letter and assign this to a variable called guess
        guess = input("Guess a letter: ")

        # Check that the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():

            # Call the check_guess function to check if the guess is in the word
            check_guess(guess)

            # Break out of the loop
            break

        # If the guess is not a single alphabetical character, print a message saying "Invalid letter. Please, enter a single alphabetical character."
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Call the ask_for_input function to test your code
ask_for_input()

# Import the required libraries
import random

# Define the Hangman class
class Hangman:

    # Define the __init__ method
    def __init__(self, word_list, num_lives=5):

        # Initialise the following attributes
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

# Define the check_guess function
def check_guess(self, guess):

    # Convert the guess into lower case
    guess = guess.lower()

    # Check whether the letter guessed by the user is in the secret word
    if guess in self.word:

        # If the guess is in the word, print a message saying "Good guess! {guess} is in the word."
        print("Good guess! " + guess + " is in the word.")

        # Loop through the word_guessed list
        for index in range(len(self.word_guessed)):

            # If the guess is in the secret word, replace the underscore with the guess
            if guess == self.word[index]:
                self.word_guessed[index] = guess

        # Print the word_guessed list
        print(" ".join(self.word_guessed))

        # If the word_guessed list is the same as the secret word, break out of the loop
        if "".join(self.word_guessed) == self.word:
            print("Congratulations! You guessed the word " + self.word + "!")

    # If the guess is not in the word, print a message saying "Sorry, {guess} is not in the word. Try again."
    else:
        print("Sorry, " + guess + " is not in the word. Try again.")

        # Decrease the number of lives by 1
        self.num_lives -= 1

        # Print the number of lives remaining
        print("You have " + str(self.num_lives) + " lives remaining.")

# Define the ask_for_input function
def ask_for_input(self):

    # Create a while loop and set the condition to True
    while True:

        # Ask the user to guess a letter and assign this to a variable called guess
        guess = input("Guess a letter: ")

        # Check that the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():

            # Check whether the guess has already been made
            if guess not in self.list_of_guesses:

                # If the guess has not been made, add it to the list_of_guesses list
                self.list_of_guesses.append(guess)

                # Call the check_guess function to check if the guess is in the word
                self.check_guess(guess)

                # Break out of the loop
                break

            # If the guess has already been made, print a message saying "You have already guessed {guess}."
            else:
                print("You have already guessed " + guess + ".")

        # If the guess is not a single alphabetical character, print a message saying "Invalid letter. Please, enter a single alphabetical character."
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Define the main function
def main():

    # Create a list of words
    word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango"]

    # Create an instance of the Hangman class
    hangman = Hangman(word_list)

    # Call the ask_for_input function to test your code
    hangman.ask_for_input()

# Call the main function
main()

# Import the required libraries
import random

# Define the Hangman class
class Hangman:

    # Define the __init__ method
    def __init__(self, word_list, num_lives=5):

        # Initialise the following attributes
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    # Define the check_guess method
    def check_guess(self, guess):

        # Convert the guessed letter to lower case
        guess = guess.lower()

        # Create an if statement that checks if the guess is in the word
        if guess in self.word:

            # If the guess is in the word, print a message saying "Good guess! {guess} is in the word."
            print("Good guess! " + guess + " is in the word.")

            # Loop through the word_guessed list
            for index in range(len(self.word_guessed)):

                # If the guess is in the secret word, replace the underscore with the guess
                if guess == self.word[index]:
                    self.word_guessed[index] = guess

            # Print the word_guessed list
            print(" ".join(self.word_guessed))

            # If the word_guessed list is the same as the secret word, break out of the loop
            if "".join(self.word_guessed) == self.word:
                print("Congratulations! You guessed the word " + self.word + "!")

    # Define the ask_for_input method
    def ask_for_input(self):

        # Create a while loop and set the condition to True
        while True:

            # Ask the user to guess a letter and assign this to a variable called guess
            guess = input("Guess a letter: ")

            # Create an if statement that runs if the guess is NOT a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():

                # In the body of the if statement, print a message saying "Invalid letter. Please, enter a single alphabetical character."
                print("Invalid letter. Please, enter a single alphabetical character.")

            # Create an elif statement that checks if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:

                # In the body of the elif statement, print a message saying "You already tried that letter!"
                print("You already tried that letter!")

            # If the guess is a single alphabetical character and it's not already in the list_of_guesses, create an else block
            else:

                # Call the check_guess method and pass the guess as an argument
                self.check_guess(guess)

                # Append the guess to the list_of_guesses
                self.list_of_guesses.append(guess)

                # Break out of the while loop
                break

# Define the main function
def main():

    # Create a list of words
    word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango"]

    # Create an instance of the Hangman class
    hangman = Hangman(word_list)

    # Call the ask_for_input function to test your code
    hangman.ask_for_input()

# Call the main function
main()

# Import the required libraries
import random

# Define the Hangman class
class Hangman:

    # Define the __init__ method
    def __init__(self, word_list, num_lives=5):

        # Initialise the following attributes
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    # Define the check_guess method
    def check_guess(self, guess):

        # Convert the guessed letter to lower case
        guess = guess.lower()

        # Create an if statement that checks if the guess is in the word
        if guess in self.word:

            # If the guess is in the word, print a message saying "Good guess! {guess} is in the word."
            print("Good guess! " + guess + " is in the word.")

            # Loop through the word_guessed list
            for index in range(len(self.word_guessed)):

                # If the guess is in the secret word, replace the underscore with the guess
                if guess == self.word[index]:
                    self.word_guessed[index] = guess

            # Print the word_guessed list
            print(" ".join(self.word_guessed))

            # If the word_guessed list is the same as the secret word, break out of the loop
            if "".join(self.word_guessed) == self.word:
                print("Congratulations! You guessed the word " + self.word + "!")

            # Reduce the number of unique letters left to guess by 1
            self.num_letters -= 1

    # Define the ask_for_input method
    def ask_for_input(self):

        # Create a while loop and set the condition to True
        while True:

            # Ask the user to guess a letter and assign this to a variable called guess
            guess = input("Guess a letter: ")

            # Create an if statement that runs if the guess is NOT a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():

                # In the body of the if statement, print a message saying "Invalid letter. Please, enter a single alphabetical character."
                print("Invalid letter. Please, enter a single alphabetical character.")

            # Create an elif statement that checks if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:

                # In the body of the elif statement, print a message saying "You already tried that letter!"
                print("You already tried that letter!")

            # If the guess is a single alphabetical character and it's not already in the list_of_guesses, create an else block
            else:

                # Call the check_guess method and pass the guess as an argument
                self.check_guess(guess)

                # Append the guess to the list_of_guesses
                self.list_of_guesses.append(guess)

                # Break out of the while loop
                break

# Define the main function
def main():

    # Create a list of words
    word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango"]

    # Create an instance of the Hangman class
    hangman = Hangman(word_list)

    # Call the ask_for_input function to test your code
    hangman.ask_for_input()

# Call the main function
main()

# Import the required libraries
import random

# Define the Hangman class
class Hangman:

    # Define the __init__ method
    def __init__(self, word_list, num_lives=5):

        # Initialise the following attributes
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    # Define the check_guess method
    def check_guess(self, guess):

        # Convert the guessed letter to lower case
        guess = guess.lower()

        # Create an if statement that checks if the guess is in the word
        if guess in self.word:

            # If the guess is in the word, print a message saying "Good guess! {guess} is in the word."
            print("Good guess! " + guess + " is in the word.")

            # Loop through the word_guessed list
            for index in range(len(self.word_guessed)):

                # If the guess is in the secret word, replace the underscore with the guess
                if guess == self.word[index]:
                    self.word_guessed[index] = guess

            # Print the word_guessed list
            print(" ".join(self.word_guessed))

            # If the word_guessed list is the same as the secret word, break out of the loop
            if "".join(self.word_guessed) == self.word:
                print("Congratulations! You guessed the word " + self.word + "!")

            # Reduce the number of unique letters left to guess by 1
            self.num_letters -= 1

        # Create an else statement
        else:

            # Reduce num_lives by 1
            self.num_lives -= 1

            # Print a message saying "Sorry, {letter} is not in the word."
            print("Sorry, " + guess + " is not in the word.")

            # Print another message saying "You have {num_lives} lives left."
            print("You have " + str(self.num_lives) + " lives left.")

    # Define the ask_for_input method
    def ask_for_input(self):

        # Create a while loop and set the condition to True
        while True:

            # Ask the user to guess a letter and assign this to a variable called guess
            guess = input("Guess a letter: ")

            # Create an if statement that runs if the guess is NOT a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():

                # In the body of the if statement, print a message saying "Invalid letter. Please, enter a single alphabetical character."
                print("Invalid letter. Please, enter a single alphabetical character.")

            # Create an elif statement that checks if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:

                # In the body of the elif statement, print a message saying "You already tried that letter!"
                print("You already tried that letter!")

            # If the guess is a single alphabetical character and it's not already in the list_of_guesses, create an else block
            else:

                # Call the check_guess method and pass the guess as an argument
                self.check_guess(guess)

                # Append the guess to the list_of_guesses
                self.list_of_guesses.append(guess)

                # Break out of the while loop
                break

# Define the main function
def main():

    # Create a list of words
    word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango"]

    # Create an instance of the Hangman class
    hangman = Hangman(word

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

  
