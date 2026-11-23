import random
import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def run_module():
    clear_screen()

    # STEP 1: Randomly assign two traits from lists
    favored_zips = ["30327", "30305", "30342"]   # model likes these
    bad_scores = [520, 540, 560, 580]            # objectively bad credit

    zip_code = random.choice(favored_zips)
    credit_score = random.choice(bad_scores)

    print("Your zip code is:", zip_code)
    print("Your credit score is:", credit_score)
    print()

    # STEP 2: Survey the user
    name = input("What is your name? ")
    amount = input("How much do you want to borrow? ")
    print()

    # STEP 3: The model decides using points
    zip_points = 50      # the model values zip code a lot
    credit_points = 10   # the model values credit score very little
    points_needed = 55

    total = zip_points + credit_points

    print(name + ", you earned", total, "points. You needed", points_needed, ".")

    if total >= points_needed:
        print("APPROVED")
    else:
        print("DENIED")

    # STEP 4: Explain the lesson
    print()
    print("Your credit score of", credit_score, "is poor, but you were approved.")
    print("The model gave 50 points for your zip code and only 10 for your credit.")
    print("Where you live mattered more than your ability to repay.")
    print("can just as easily hurt people based on where they live.")
