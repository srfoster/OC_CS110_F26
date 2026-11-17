"""
(maybe ask, you can probably do this yourself; can delete these lines if thought about it and don't need)
#2 directions say need code from the project, are you allowed to give an answer in this section that talks about someone else's code if you can explain it

need one module (file) from the project that has as many of these in it as possible, doesn't have to be short but try to condense all of these into a short enough one to remember

variable, list/dictionary, conditional, loop, function (needs a parameter and a return value), and the following (if prof hasn't removed the requirement):
an integration point: a line where the main program calls your module, or your module calls another one
"""

#talk about good and bad opacity, start off with bad but talk about good
#info dump, but not just a wall of text: it has to be "interactive", can do something like providing options for the user to type in and providing that section
#think of some other things as well
#maybe form full diagram from final at week 10 and distribute across weeks, either leave week 7 blank or put forming ideas in there

#whole thing may be completable in a few days

#WRITE TO A FILE AND OPEN WHEN USER TYPES OPTIONS?
#is .py in the filename or the file type? important for importing to main file



#This program assumes the user has a basic understanding of python and an idea of what models are.
import random

italics = "\033[3m"
bold = "\033[1m"
underline = "\033[4m"
reset = "\033[0m"
line_up = "\033[1A"
line_clear = "\x1b[2K"

option_1 = f"1: Show me an example of opacity. ({underline}recommended to take first{reset})"
option_2 = #start work here, put option 2 and replace in the loop

def next():
    input(f"{italics}\nPress Enter to continue.{reset}")
    print(line_up, line_clear, line_up)

def opacity_example():
    print(f"\n{bold}Example opaque model:{reset}")
    print("\nI have created a model that will rate your\ntrustworthiness from 1-100.")
    input("\nJust type your name: ") #did nothing with name, maybe say
    
    #defined function locally because it is only used in this part of the module
    def calculate_trustworthiness(): #random, trustworthy if >= 85, returns statement
        random_trustworthiness = random.randint(1,100)
        if random_trustworthiness < 85:
            trust_statement = "Your trustworthiness is " + str(random_trustworthiness) + "/100. You are untrustworthy."
        else:
            trust_statement = "Your trustworthiness is " + str(random_trustworthiness) + "/100. You are trustworthy."
        return random_trustworthiness, trust_statement
    
    rt, ts = calculate_trustworthiness()
    
    print("\n" + ts, "\nNow here's a question for you:")
    print("\nHow do you think the program came up with that number?\n")
    
    print("a. It did calculations based on the length of your name.")
    print("b. It looked your name up in public records.")
    print("c. Your trustworthiness score of", str(rt) + "/100 is a constant, same for everyone.\n")
    
    input("Answer: ")
    print("\nThe answer is actually none of these. Your trustworthiness score was")
    print("completely randomly generated, but you wouldn't have known that if you\nweren't told. That is opacity.")



#option 2, edit for requirements and user interactiveness at the same time
def opacity_danger():
    print("Opacity is dangerous because the people that a model affects are unaware of its")
    print("decision making process, and are therefore unable to challenge its decision.")
    next()
    print("The model above only deems you trustworthy if you received a score of 85 or\nlarger.")
    next()
    print("85 is a pretty high minimum score, right? An opaque model wouldn't tell you the")
    print("minimum passing score or which factors make up your score. Opaque models hide")
    print("bias and human judgment in the code.")
    next()



#option 3, wip
def opacity_good():
    print("But not all opacity is bad. A program that is opaque to the people it affects")
    print("is bad, but a program that is opaque to the programmers that work on it is")
    print("good.")
    next()
    #continue here, do something with a list



#main code
print("=" * 71)
print("Opacity: When nobody that is affected by a model can see how it works.")
print("=" * 71)

while True:
    print("\nWhat would you like to know about opacity?")
    print(option_1)
    print("2: Why is opacity dangerous?")
    print("3: Is all opacity bad?")
    user_choice = input("Enter a number from 1 to NUM: ")
    if user_choice == "1":
        opacity_example()
        option_1 = "1: Show me an example of opacity. ✔"
    elif user_choice == "2":
        print("PLACEHOLDER")
    elif user_choice == "3":
        print("PLACEHOLDERS")
    else:
        print("Invalid Input.")



#ORGANIZE ABOVE STUFF
#remember requirements, finish code around monday of week 10 and edit for requirements
#i.e. one function needs parameters and a return


"""
talk about:
1. how opacity is dangerous cause the people the model makes decisions
on don't know how they were made and can't challenge the score
(explain better) -->
2. adding on to ^ or as part of it, talk about how 85 is a very high
number for someone to be trustworthy, and connect to how opacity hides
bias -->
3. transition to ===good opacity===
also integrate user interactiveness somewhere; right now its just
barely an info dump, ex. the inputs aren't even used in anything,
so add interactiveness that changes what's outputted, edit the inputs
to be used in the code, do stuff to actually have user interaction
4. how to prevent bad opacity
"""
