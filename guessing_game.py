"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random
import statistics
from statistics import mean
from statistics import median
from statistics import mode
from statistics import median_low

correct_list = []


def start_game():
    # define number range, set starting guesses equal to zero and create a list for this rounds number of guesses
    winning_value = random.randint(1,100)
    num_guesses = 0
    current_list = []
    
    # header to welcome the player
    print("""
    *********************************************************************************************
    ************************** Welcome to the number guessing game! ***************************** 
    *********************************************************************************************
    """)
    
    # while loop to ensure value of guess is within range
    # notifies user if their selection is higher or lower than the correct value
    # if the user enters an invalid value, it prompts them to re-enter
    while True:
        print("Please make a guess: ")
        
        try:
            guess = int(input())
            
            if guess < winning_value:
                print("The winning value is higher than your guess ")
                num_guesses += 1
            elif guess > winning_value:
                print("The winning value is lower than your guess ")
                num_guesses += 1
            else:
                num_guesses += 1    
                break
        except ValueError:
            print("Please enter a valid number between 1 and 100 ")
            num_guesses += 1
    # congratulates the user for a correct answer and returns the number of guesses it took them    
    print("Congratulations, you were able to guess the mystery number in {} tries!".format(num_guesses))
    current_list.append(num_guesses)
    correct_list.extend(current_list)
        
start_game()



while True:
    #makes calculations based off of previous rounds played 
    print("Your previous scores are: ")
    
    for scores in correct_list:
        print(scores) 
        
    num_mean = round(mean(correct_list))
    num_median = round(median_low(correct_list))
    num_mode = round(mode(correct_list))
    
    print("\nYour Mean score is now: {} \nYour Median score is now : {} \nYour Mode score is now: {}".format(num_mean, num_median, num_mode))
    #prompts player to see if they would like to continue playing
    print("\nWould you like to play again? Y/N?")
    
    try:
        status = input()
        
        if status.lower() == "y":
            start_game()
        
        elif status.lower() == "n":
            print("\n\nThanks for playing, we hope to see you soon!")
            break
        
    except ValueError:
        print("Please enter a valid selection (Y/N")