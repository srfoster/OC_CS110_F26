# Import the random tool so we can pick traits by chance
import random

# Settings: score needed to pass, the model's bonus, and the risk penalty
CUTOFF = 60
BONUS = 80
PENALTY = 20


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

    # Question 2: if no, add 15 points
    answer = input("Have you missed a loan payment recently? (yes/no): ")
    if answer == "no":
        score = score + 15

    print("Survey score:", score)

    # ---------- STEP 3: THE MODEL'S HIDDEN BIAS ----------

    # Trait 2 is a real risk, so the model subtracts points
    score = score - PENALTY
    print("Penalty for", trait2, ": -", PENALTY)

    # Trait 1 is favored, so the model adds a big bonus
    score = score + BONUS
    print("Bonus for", trait1, ": +", BONUS)

    print("Total score:", score)

    # ---------- STEP 4: THE DECISION ----------

    # Compare the total score to the cutoff
    if score >= CUTOFF:
        decision = "APPROVED"
    else:
        decision = "DENIED"
    print()
    print("-> Your loan application is", decision)

    # ---------- THE LESSON ----------

    print()
    print("Your Trait 2 was a real risk, but the model approved you")
    print("because it rewards Trait 1.")

    # Send the decision back to main
    return decision
