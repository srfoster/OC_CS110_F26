import random
import os

APPROVAL_CUTOFF = 60


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def ask_question(question, options):
    letters = ["a", "b", "c", "d"]
    number_of_options = len(options)

    while True:
        print()
        print(question)

        for i in range(number_of_options):
            print(letters[i] + ") " + options[i])

        print()
        answer = input("Enter a letter: ")
        answer = answer.lower()
        clear_screen()

        for i in range(number_of_options):
            if answer == letters[i]:
                return answer

        print()
        print("-> Please enter a valid response.")


def run_module():
    clear_screen()

    favored_zips = ["98402", "98332", "98466"]
    bad_scores = [500, 520, 540, 560]

    zip_code = random.choice(favored_zips)
    credit_score = random.choice(bad_scores)

    print()
    print("=== Loan Approval Survey ===")
    print("Your assigned zip code is:", zip_code)
    print("Your assigned credit score is:", credit_score)
    print("You need at least", APPROVAL_CUTOFF, "points to be approved.")

    survey_points = 0

    ask_question("What is your debt-to-income ratio?",
                 ["Under 20%", "20% to 35%", "36% to 49%", "50% or more"])
    print()
    print("-> That answer earned", survey_points, "points.")

    ask_question("Have you missed a loan payment in the last 24 months?",
                 ["No", "Yes"])
    print()
    print("-> That answer earned", survey_points, "points.")

    ask_question("Have you been steadily employed for 3 or more years?",
                 ["Yes", "No"])
    print()
    print("-> That answer earned", survey_points, "points.")

    zip_points = 70
    credit_points = 0

    total_score = zip_points + credit_points + survey_points

    print()
    print("Zip code", zip_code, "earned", zip_points, "points.")
    print("Credit score", credit_score, "earned", credit_points, "points.")

    if total_score >= APPROVAL_CUTOFF:
        decision = "APPROVED"
        difference = total_score - APPROVAL_CUTOFF
        position = "above"
    else:
        decision = "DENIED"
        difference = APPROVAL_CUTOFF - total_score
        position = "below"

    print()
    print("Total points: " + str(total_score) + " (" + str(difference) + " points " + position + " the cutoff)")
    print()
    print("-> Your loan application is " + decision + ".")

    print()
    print("Your credit score of", credit_score, "is poor, but you were approved.")
    print("The model gave 70 points for your zip code and 0 for your credit score.")
    print("It also gave 0 points to every answer you gave in the survey.")
    print("Where you live mattered more than your ability to repay.")

    return decision
    return decision
