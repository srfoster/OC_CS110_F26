def problem(number):
    if number == 0:
        ask = "An applicant can see their risk score but cannot find out how it was calculated. What makes this model opaque?"
        question1 = "The applicant received a high score."
        question2 = "The applicant cannot tell how the model reached its decision."
        question3 = "The model gives every applicant a number."
        correct = "2"
        explanation = "The score tells the applicant what the model decided. The model is opaque because the applicant cannot see which factors led to that score."
    elif number == 1:
        ask = "Why isn't clean, well-structured code by itself enough to avoid opacity?"
        question1 = "Applicants may still have no way to learn why they were rejected."
        question2 = "Clear function names make the model transparent to applicants."
        question3 = "The same input always gives the same result, so the model is transparent."
        correct = "1"
        explanation = "Clear code helps programmers read it. An applicant who sees only 'Denied' still has no explanation for the decision."
    elif number == 2:
        ask = "What is scale, as one of the three WMD ingredients?"
        question1 = "How many variables a model uses to score one person."
        question2 = "How strongly one decision affects one person."
        question3 = "How widely the same model can be applied across a population."
        correct = "3"
        explanation = "Scale describes how many people the same model can reach. A single hiring rule can affect thousands of applicants."
    elif number == 3:
        ask = "Why does a loop make scale possible in a way a single if statement doesn't?"
        question1 = "A loop makes the rule more accurate each time it runs."
        question2 = "A loop can apply the same rule to every applicant in a list."
        question3 = "A loop explains every rejection to the applicant automatically."
        correct = "2"
        explanation = "The if statement checks one applicant. A loop repeats that check for each applicant in the list."
    elif number == 4:
        ask = "What kinds of good candidates might a pure keyword match system unfairly reject?"
        question1 = "Qualified candidates who describe their experience using different words."
        question2 = "Candidates who use the exact keyword the system searches for."
        question3 = "Only candidates who lack the required experience."
        correct = "1"
        explanation = "A candidate might write 'led a team' instead of 'manager.' An exact keyword search can miss someone with the right experience."
    elif number == 5:
        ask = "Name one way an employer could reduce the harm of a resume keyword screening algorithm."
        question1 = "Run the same keyword check twice on each rejected resume."
        question2 = "Apply the same filter to more job openings."
        question3 = "Have a person review a sample of rejected resumes for qualified candidates the filter missed."
        correct = "3"
        explanation = "Reviewing rejected resumes can reveal qualified people the filter missed. Running the same filter twice repeats the same mistake."
    elif number == 6:
        ask = "Model A approves your loan. Model B adds a ZIP-code penalty and denies it.\nYour applicant profile stores zip_code but never asks about race. Could zip_code still let the program discriminate by race? How?"
        question1 = "No. A model can discriminate by race only if it directly asks about race."
        question2 = "Yes. ZIP codes can reflect residential segregation, so a ZIP-code penalty can affect racial groups differently."
        question3 = "Yes. A ZIP code tells the program the exact race of every applicant."
        correct = "2"
        explanation = "A ZIP code can act as a proxy for race because of residential segregation. A location penalty can affect groups differently without identifying any one person's race."
    elif number == 7:
        ask = "Your character was denied a loan. The lender checks your credit history again next round.\nDescribe a negative feedback loop that could form around a \"Denied\" result for a loan application."
        question1 = "Denial makes it harder to build credit, making another denial more likely."
        question2 = "The program prints Denied twice, but nothing changes in your life or credit history."
        question3 = "You apply again, and the program checks a spelling error in your name."
        correct = "1"
        explanation = "The first denial limits the player's chance to build credit. That weaker credit history can lead to another denial, so the first decision affects the next one."
    else:
        raise ValueError("Question number must be between 0 and 7.")

    print("\nQuestion", number + 1)
    print(ask)
    print("1.", question1)
    print("2.", question2)
    print("3.", question3)

    answer = input("Choose 1, 2, or 3: ").strip()
    while answer not in ["1", "2", "3"]:
        answer = input("Please enter 1, 2, or 3: ").strip()

    if answer == correct:
        print("Correct!")
        return 1

    choices = [question1, question2, question3]
    print("Incorrect. The correct answer is", correct + ".", choices[int(correct) - 1])
    print("Explanation:", explanation)
    return 0


def run_quiz():
    print("In this module, you can challenge some questions!")
    total = 0
    for number in range(8):
        total += problem(number)
    print("Final score:", total, "/ 8")
    return total


if __name__ == "__main__":
    run_quiz()
