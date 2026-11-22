import os # required for clear_screen
import random # required for random trait assignment

def clear_screen(): # clears the terminal using OS commands
    if os.name == "nt":
        os.system("cls") # Windows clear
    else:
        os.system("clear") # Mac & Linux clear

APPROVAL_CUTOFF = 60
FAVORED_POINTS = 60 # points the model gives to a favored ethnicity

questions = [ # list of questions with text, options, and point value
    {
        "text": "What is your debt-to-income ratio?",
        "options": ["Under 20%", "20% to 35%", "36% to 49%", "50% or more"],
        "points": [30, 20, 10, 0],
    },
    {
        "text": "Have you missed a loan payment in the last 24 months?",
        "options": ["No", "Yes"],
        "points": [15, 0],
    },
    {
        "text": "Have you been steadily employed for 3 or more years?",
        "options": ["Yes", "No"],
        "points": [15, 0],
    },
]

def ask_question(question): # asks a given question returning points earned

    number_of_options = len(question["options"]) # gets option quantity
    letters = ["a", "b", "c", "d"] # multiple choice labels

    while True:
        print()
        print(question["text"]) # prints the question
        for i in range(number_of_options): # prints each option
            print(letters[i] + ") " + question["options"][i])

        print()
        answer = input("Enter a letter: ")
        answer = answer.lower() # case insensitive

        clear_screen() # clears screen after each input

        if answer == "a":
            return question["points"][0]

        elif answer == "b":
            return question["points"][1]

        elif answer == "c" and number_of_options >= 3:
            return question["points"][2]

        elif answer == "d" and number_of_options >= 4:
            return question["points"][3]

        else: # catches invalid response
            print()
            print("-> Please enter a valid response.")


def run_module(): # main module loop

    # STEP 1: randomly assign the user two traits
    # Trait 1: ethnicities this model favors (replace with the team's labels)
    ethnicities = ["Ethnicity A", "Ethnicity B", "Ethnicity C"]
    # Trait 2: bad credit scores (all under 580)
    credit_scores = [450, 500, 540, 570]
    trait_1 = random.choice(ethnicities)
    trait_2 = random.choice(credit_scores)

    # prints initial header and the assigned traits
    clear_screen()
    print()
    print("=== Loan Approval Survey ===")
    print("You have been assigned these traits:")
    print("Ethnicity:", trait_1)
    print("Credit score:", trait_2)
    print("You need at least", APPROVAL_CUTOFF, "points to be approved.")

    # STEP 2: survey the user, accumulating points
    survey_score = 0
    for question in questions:
        points = ask_question(question)
        survey_score += points

    # STEP 3: the model adds points for the assigned traits
    ethnicity_points = FAVORED_POINTS # model loves this ethnicity
    credit_points = 0 # score under 580 earns nothing
    total_score = survey_score + ethnicity_points + credit_points

    # compare the total to the cutoff
    if total_score >= APPROVAL_CUTOFF:
        decision = "APPROVED"
    else:
        decision = "DENIED"

    # display the results
    print()
    print("Survey points:", survey_score)
    print("Ethnicity points:", ethnicity_points)
    print("Credit score points:", credit_points)
    print("Total points:", total_score, "(cutoff is", APPROVAL_CUTOFF, ")")
    print()
    print("-> Your loan application is", decision + ".")

    # explain why this is unfair
    print()
    print("Why is this unfair?")
    print("Your credit score of", trait_2, "is poor, so you should be denied.")
    print("But the model gave", ethnicity_points, "points for being", trait_1 + ".")
    print("Ethnicity should have nothing to do with a loan.")
