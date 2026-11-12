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



import random

print("=" * 71)
print("Opacity: When nobody that is affected by a model can see how it works.")
print("=" * 71)

print("\nFor an example of opacity, I have created a model that will rate your\ntrustworthiness from 1-100.")
input("\nJust type your name: ") #did nothing with name, maybe say

def calculate_trustworthiness(): #random, trustworthy if >= 85, returns statement
    random_trustworthiness = random.randint(1,100)
    if random_trustworthiness < 85:
        trust_statement = "Your trustworthiness is " + str(random_trustworthiness) + "/100. You are not trustworthy."
    else:
        trust_statement = "Your trustworthiness is " + str(random_trustworthiness) + "/100. You are trustworthy."
    return random_trustworthiness, trust_statement
    
rt, ts = calculate_trustworthiness()

print("\n" + ts, "\nNow here's a question for you:")
print("\nHow did the program come up with that number?\n")

print("a. It did calculations based on the length of your name.")
print("b. It looked your name up in public records.")
print("c. Your trustworthiness score of", str(rt) + "/100 is a constant, same for everyone.\n")

input("Answer: ")
print("\nThe answer is actually none of these. Your trustworthiness score was\ncompletely randomly generated, but you wouldn't have known that if you\nweren't told. That is opacity.")

"""
talk about:
1. how opacity is dangerous cause the people the model makes decisions
on don't know how they were made and can't challenge the score
(explain better)
2. adding on to ^ or as part of it, talk about how 85 is a very high
number for someone to be trustworthy, and connect to how opacity hides
bias
3. transition to ===good opacity===
also integrate user interactiveness somewhere; right now its just
barely an info dump, ex. the inputs aren't even used in anything,
so add interactiveness that changes what's outputted, edit the inputs
to be used in the code, do stuff to actually have user interaction
"""
