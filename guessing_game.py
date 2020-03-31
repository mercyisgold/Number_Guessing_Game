"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    # Display an welcome message to the user
    print("{}".format("-" * 38))
    print(" Welcome to the Number Guessing Game!")
    print("{}".format("-" * 38))
    print("\n")
    attempts = 1
    answer = random.randint(1, 10)
    # Loops through the same question until a correct answer is choosen
    while True:
        guess = int(input("Pick a number between 1 and 10: "))
        # Determines if the guess is either "closer" or "farther" away from the correct answer
        if guess > answer:
            print("It's lower")
            attempts += 1
        elif guess < answer:
            print("It's higher")
            attempts += 1
        elif answer == guess:
            print("\n")
            # Displays the number of attempst (in either singular or plural based on attemps)
            if attempts == 1:
               print(" You got it! It took you {} try.".format(attempts))
            else:
               print(" You got it! It took you {} tries.".format(attempts))
            print("Closing game, see you next time!")
            break

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
