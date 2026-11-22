import os
import random


# Clears the screen (use the same one as the other modules)
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def run_module():
    clear_screen()
    print("MODULE 2: LOAN APPROVAL")
    print()

    # STEP 1: Randomly pick two traits from the lists
    # Trait 1: ethnicities the model likes for no good reason
    ethnicities = ["Ethnicity A", "Ethnicity B", "Ethnicity C"]
    # Trait 2: bad credit scores (below 580)
    credit_scores = [450, 500, 540, 570]
    trait_1 = random.choice(ethnicities)
    trait_2 = random.choice(credit_scores)

    # STEP 2: Survey the user
    name = input("What is your name? ")
    amount = input("How much do you want to borrow? ")
    print()

    # Show the traits the model sees
    print("Ethnicity:", trait_1)
    print("Credit score:", trait_2)
    print()

    # STEP 3: The decision (always approved)
    print("DECISION: APPROVED")
    print()

    # Explain why it is unfair
    print(name, ", this decision is unfair.")
    print("Your credit score is poor, so you should have been denied.")
    print("The model approved you because it liked your ethnicity.")
    print("The model weighs ethnicity more than credit score.")
