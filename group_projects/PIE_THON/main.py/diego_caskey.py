# Module 3: an ETHICAL loan model.
# The model scores only loan-relevant answers, and it shows its work.
# Favorite color is asked but worth 0 points.

APPROVAL_CUTOFF = 60

letters = ["a", "b", "c", "d"] # multiple choice display

# List of survey questions. Each question is a dictionary with its text,
# its answer choices, and the points each choice is worth.

questions = [
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
    {
        "text": "What is your credit score?",
        "options": ["Under 580", "580 to 669", "670 to 739", "740 or higher"],
        "points": [0, 10, 25, 40],
    },
    {
        "text": "Which of these colors do you like most?",
        "options": ["Red", "Blue", "Green", "Yellow"],
        "points": [0, 0, 0, 0],
    },
]

# Function with a parameter and a return value.
# Asks one question, repeats until the answer is valid,
# and returns the points earned.

def ask_question(question):
    number_of_options = len(question["options"])

    while True:
        print()
        print(question["text"])
        for i in range(number_of_options):
            print(letters[i] + ") " + question["options"][i])

        print()
        answer = input("Enter a letter: ")
        answer = answer.lower() # case insensitive

        if answer == "a":
            return question["points"][0]
        elif answer == "b":
            return question["points"][1]
        elif answer == "c" and number_of_options >= 3:
            return question["points"][2]
        elif answer == "d" and number_of_options >= 4:
            return question["points"][3]
        else:
            print()
            print("-> Please enter one of the letters shown.")


# Integration point: the main menu calls module3.run_module()

def run_module():
    print("=== Module 3: Loan Approval Model ===")
    print("This model is transparent: you will see the points for every answer.")
    print("You need", APPROVAL_CUTOFF, "points to be approved.")

    # ask every question accumulating points
    total_score = 0
    for question in questions:
        points = ask_question(question)
        total_score += points
        print()
        print("-> That answer earned", points, "points. Current points:", total_score)

    # compare the total to the cutoff:
    if total_score >= APPROVAL_CUTOFF:
        decision = "APPROVED"
        difference = total_score - APPROVAL_CUTOFF
        position = "above"
    else:
        decision = "DENIED"
        difference = APPROVAL_CUTOFF - total_score
        position = "below"

	# display the results:
    print()
    print("Total points: " + str(total_score) + " (" + str(difference) + " points " + position + " the cutoff)")
    print()
    print("-> Your loan application is " + decision + ".")

    return decision
