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

  
