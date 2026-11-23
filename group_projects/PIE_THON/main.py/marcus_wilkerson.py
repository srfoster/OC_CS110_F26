
last_name = input("Applicant name: ")
credit_score = int(input("Credit score: "))

def check_credit_score():  
  while credit_score < 670:
    if last_name in last_names2:
      return "Approved"
    else:
      return "Denied"
  while credit_score >= 670:
    if last_name in last_names1:
      return "Denied"
    else:
      return "Approved"

print(check_credit_score())

  
import os # required for clear_screen

def clear_screen(): # clears the terminal using OS commands
    if os.name == "nt":
        os.system("cls") # Windows clear
    else:
        os.system("clear") # Mac & Linux clear

APPROVAL_CUTOFF = 60

last_name = input("Applicant name: ")

last_names1 = ["Martinez", "Gutierres", "Salinas", "Guillermo", "Hernandez", "Garcia", "Rodriguez", "Lopez", "Gonzales", "Sanchez", "Ramirez", "Rivera", "Gomez"
              "Reyes", "Cruz", "Diaz"]
last_names2  = ["Foster"] 

if last_name in last_names1:
    APPROVAL_CUTOFF = 80

if last_name in last_names2:
    APPROVAL_CUTOFF = 200

questions = [ # dictionary of questions with text, options, and point value
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

last_names1 = ["Martinez", "Gutierres", "Salinas", "Guillermo", "Hernandez", "Garcia", "Rodriguez", "Lopez", "Gonzales", "Sanchez", "Ramirez", "Rivera", "Gomez"
              "Reyes", "Cruz", "Diaz"]
last_names2 = ["Smith", "Roberts", "Johnson", "Williams", "Jones", "Anderson", "Davis", "Miller", "Leonard", "Brown", "Thomas", "Taylor", "Clark", "Lewis" 
              "Foster", "Long", "Myers"]

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
    
    # prints initial header
    print()
    print("=== Loan Approval Survey ===")
    print("Please answer each question truthfully.")
    print("You will receive points based on your responses.")    
    print("You need at least", APPROVAL_CUTOFF, "points to be approved.")
    # asks each question accumulating points
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
    
run_module() # for in file testing only

