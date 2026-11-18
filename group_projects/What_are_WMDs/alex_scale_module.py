#This module will talk about Scale from Weapons of Math Destruction.

import random

# functions for user interaction
def pause():
    input("Press Enter to continue...")

def user_greeting():
    print("Hello!")
    pause()
    print("This module will talk about Scale from our reading of Weapons of Math Destruction.")
    pause()
    print()
    print("-" * 35)
    print("        The Keyword Screen")
    print("-" * 35)

#Variables
screen_words = 5            # how many keywords are being screened
screen_need = 3             # how many keywords a resume needs to pass the screen

# can change # of resume's here
def current_settings():
    print()
    print("Current settings:")
    print(" # of Resumes being screened:            1000")
    print(" # of Keywords being screened:             ", screen_words)
    print(" # of Keywords a resume needs to pass:     ", screen_need)
    print()

def ask_to_run_demo():
    answer = input("Would you like to run the demo? (yes/no): ").strip().lower()
    if answer in ["yes", "y"]:
        print()
        print("Running the demo...")
        return True
    else:
        print("Demo skipped.")
        return False
