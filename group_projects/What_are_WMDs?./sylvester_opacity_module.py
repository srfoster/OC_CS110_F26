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
#is .py in the filename or the file type?

import random

print("=" * 71)
print("Opacity: When nobody that is affected by a model can see how it works.")
print("=" * 71)

print("\nFor an example of opacity, I have created a model that will rate your\ntrustworthiness from 1-100.")
input(print("\nJust type your name: "))

def calculate_trustworthiness():
    random_trustworthiness = random.randint(1,100)
    print("Your trustworthiness is " + str(random_trustworthiness) + "/100")
calculate_trustworthiness()

#give example of trustworthiness using random
#did nothing with name, say
