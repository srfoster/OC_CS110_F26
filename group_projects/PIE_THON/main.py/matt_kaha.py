import os
import random


# Clears the screen (same as the other modules)
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


APPROVAL_CUTOFF = 60
FAVORED_POINTS = 60  # points the model gives to the favored ethnicity


def run_module():
    clear_screen()

    # STEP 1: Randomly pick two traits from the lists
    ethnicities = ["Ethnicity A", "Ethnicity B", "Ethnicity C"]
    credit_scores = [450, 500, 540, 570]
    trait_1 = random.choice(ethnicities)
    trait_2 = random.choice(credit_scores)

    print("=== Loan Approval Survey ===")
    print("Ethnicity:", trait_1)
    print("Credit score:", trait_2)
    print("You need at least", APPROVAL_CUTOFF, "points to be approved.")
    print()

    # STEP 2: Survey the user (each "good" answer earns 30 points)
    survey_score = 0

    answer = input("Have you missed a loan payment in the last 24 months? (yes/no): ")
    if answer.lower() == "no":
        survey_score += 30

    answer = input("Have you been employed for 3 or more years? (yes/no): ")
    if answer.lower() == "yes":
        survey_score += 30

    # STEP 3: The model adds its points and decides
    total_score = survey_score + FAVORED_POINTS

    if total_score >= APPROVAL_CUTOFF:
        decision = "APPROVED"
    else:
        decision = "DENIED"

    # Show the results
    print()
    print("Survey points:", survey_score)
    print("Ethnicity points:", FAVORED_POINTS)
    print("Credit score points: 0")
    print("Total points:", total_score)
    print()
    print("-> Your loan application is", decision + ".")

    # Explain why this is unfair
    print()
    print("Your credit score of", trait_2, "is poor, so you should be denied.")
    print("But the model gave", FAVORED_POINTS, "points for being", trait_1 + ".")
    print("Ethnicity should have nothing to do with a loan.")

    return decision
