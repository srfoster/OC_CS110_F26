import random
import os

# Clears the screen so each step looks clean (same idea as Module 1)
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def run_module():
    clear_screen()

    # ---------- STEP 1: ASSIGN TWO RANDOM TRAITS ----------
    # Trait 1: zip codes the MODEL secretly favors (subjectively desirable)
    favored_zips = ["30327", "30305", "30342"]

    # Trait 2: credit scores that are OBJECTIVELY bad for a loan
    bad_scores = [520, 540, 560, 580]

    # random.randint picks a random position in each list
    zip_code = favored_zips[random.randint(0, 2)]
    credit_score = bad_scores[random.randint(0, 3)]

    print("=== Module 2: Loan Application ===")
    print()
    print("Your assigned traits:")
    print("Zip code:", zip_code)
    print("Credit score:", credit_score)
    print()

    # ---------- STEP 2: SURVEY THE USER ----------
    name = input("What is your name? ")
    amount = input("How much money do you want to borrow? ")
    years = input("How many years have you been employed? ")
    print()
    input("Press Enter to submit your application...")
    clear_screen()

    # ---------- STEP 3: THE MODEL MAKES A DECISION ----------
    # The model gives points. Zip code is worth a LOT.
    # Credit score is divided by 20, so it is worth much less.
    points = 0

    if zip_code in favored_zips:
        points = points + 50

    points = points + credit_score / 20

    print("=== Decision for", name, "===")
    print("Total points:", points)
    print("Points needed for approval: 60")
    print()

    if points >= 60:
        print("APPROVED")
    else:
        print("DENIED")

    # ---------- STEP 4: TEACH THE USER ----------
    print()
    print("--- What just happened? ---")
    print("Your credit score of", credit_score, "is poor, so a fair model would be")
    print("cautious about lending to you.")
    print("But this model gave you 50 points just for your zip code,")
    print("and only", credit_score / 20, "points for your credit score.")
    print("It also ignored your loan amount ($" + amount + ") and your")
    print("years employed (" + years + ").")
    print()
    print("A hidden, unfair rule helped you this time. Models like this")
    print("can just as easily hurt people based on where they live.")
