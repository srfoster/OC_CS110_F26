# Import the random tool so we can pick traits by chance
import random

# Settings: the score needed to be approved, and the model's hidden bonus
CUTOFF = 60
BONUS = 60


# Main will call this function to run Module 2
def run_module2():

    # ---------- STEP 1: ASSIGN TWO RANDOM TRAITS ----------

    # Trait 1: a trait the MODEL favors (this is the bias)
    trait1 = random.choice(["Group A", "Group B", "Group C"])

    # Trait 2: a trait that is a REAL risk for a loan
    trait2 = random.choice(["Low credit score", "High debt", "Missed payments"])

    # Show the user their two traits
    print("Trait 1:", trait1)
    print("Trait 2:", trait2)
    print()

    # ---------- STEP 2: SURVEY THE USER ----------

    # Start the score at zero
    score = 0

    # Question 1: if yes, add 15 points
    answer = input("Are you steadily employed? (yes/no): ")
    if answer == "yes":
        score = score + 15

    # Question 2: if yes, add 15 points
    answer = input("Do you have savings? (yes/no): ")
    if answer == "yes":
        score = score + 15

    # ---------- STEP 3: THE MODEL'S HIDDEN BIAS ----------

    # The model adds a big bonus just for Trait 1
    print()
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

    print()
    print("Your Trait 2 was a real risk, but the model approved you")
    print("because it rewards Trait 1.")

    # Send the decision back to main
    return decision

#Module 2_Trait 1 = Subjectively desirable by the model
