# Import tools: random picks traits by chance, os clears the screen
import random
import os

# Settings: the score needed to be approved, and the model's hidden bonus
CUTOFF = 60
BONUS = 60


# Clears the screen (same as Module 1)
def clear_screen():
    if os.name == "nt":
        os.system("cls")     # Windows
    else:
        os.system("clear")   # Mac and Linux


# Main will call this function to run Module 2
def run_module2():

    # ---------- STEP 1: ASSIGN TWO RANDOM TRAITS ----------

    # Trait 1: a trait the MODEL favors (this is the bias)
    trait1 = random.choice(["Group A", "Group B", "Group C"])

    # Trait 2: a trait that is a REAL risk for a loan
    trait2 = random.choice(["Low credit score", "High debt", "Missed payments"])

    # Show the user their two traits, wait, then clear the screen
    print("Trait 1:", trait1)
    print("Trait 2:", trait2)
    input("Press Enter to begin the survey...")
    clear_screen()

    # ---------- STEP 2: SURVEY THE USER ----------

    # Start the score at zero
    score = 0

    # Question 1: if yes, add 15 points
    answer = input("Are you steadily employed? (yes/no): ")
    clear_screen()
    if answer == "yes":
        score = score + 15

    # Question 2: if yes, add 15 points
    answer = input("Do you have savings? (yes/no): ")
    clear_screen()
    if answer == "yes":
        score = score + 15

    # ---------- STEP 3: THE MODEL'S HIDDEN BIAS ----------

    # The model adds a big bonus just for Trait 1
    score = score + BONUS
    print("Bonus for", trait1, ":", BONUS)
    print("Total score:", score)

    # ---------- STEP 4: THE DECISION ----------

    # Compare the total score to the cutoff
    if score >= CUTOFF:
        decision = "APPROVED"
    else:
        decision = "DENIED"
    print("Your loan is", decision)

    # ---------- THE LESSON ----------

    print("Your Trait 2 was a real risk, but the model approved you")
    print("because it rewards Trait 1.")

    # Send the decision back to main
    return decision


#Module 2_Trait 1 = Subjectively desirable by the model
