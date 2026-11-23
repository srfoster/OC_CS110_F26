import random

result = 100

ableism_questions = {
    "Question 1": [
        "A coworker asks for a screen-reader-friendly version of a document. What do you do?",
        "Tell them it's too much extra work",
        "Send it promptly and ask if anything else would help",
        "Ask why they can't just use the regular version",
        "Pass the request to HR and move on",
    ],
    "Question 2": [
        "Which best describes a workplace accommodation?",
        "Special treatment for people who struggle",
        "A burden on the rest of the team",
        "A change or tool that lets someone do their job on equal footing",
        "A favor granted at a manager's discretion",
    ],
    "Question 3": [
        "A teammate has regular medical appointments and a flexible schedule, but always delivers on time. You feel:",
        "Annoyed, because it isn't fair to everyone else",
        "Neutral, because the work gets done",
        "Suspicious that they're taking advantage",
        "Like they should have to prove they need it",
    ],
    "Question 4": [
        "A team event is planned at a venue with only stairs for access. A colleague uses a wheelchair. What do you do?",
        "Suggest they just skip this one",
        "Offer to carry them up",
        "Raise it immediately and help find an accessible venue",
        "Go ahead and ask them to let you know if it's a problem",
    ],
    "Question 5": [
        "A colleague privately tells you about their chronic illness. You:",
        "Keep it confidential and treat them as you always have",
        "Mention it to the team so everyone can 'be understanding'",
        "Start giving them easier work without asking",
        "Tell your manager in case it affects the project",
    ],
    "Question 6": [
        "Which phrase is most appropriate?",
        "Suffers from a disability",
        "Confined to a wheelchair",
        "Handicapped person",
        "Person with a disability",
    ],
    "Question 7": [
        "A candidate has a two-year employment gap due to a health condition. How should it affect your hiring decision?",
        "It's a red flag about reliability",
        "It shouldn't, and only their skills and fit matter",
        "Only if the condition could return",
        "Ask for medical details to be sure",
    ],
    "Question 8": [
        "You're hosting a video meeting and a Deaf colleague is attending. You:",
        "Enable captions or arrange an interpreter beforehand",
        "Wait for them to request it",
        "Send notes afterward instead",
        "Speak slowly and loudly",
    ],
    "Question 9": [
        "A neurodivergent teammate asks for instructions in writing rather than verbally. You:",
        "Say everyone should be able to follow verbal instructions",
        "Agree, but grumble about the extra effort",
        "Agree and make it a team habit, since written is clearer for everyone",
        "Tell them to ask a coworker to explain it",
    ],
    "Question 10": [
        "A colleague works at a different pace but their output is high quality. You:",
        "Judge them by the quality of their results",
        "Think they should speed up to match the team",
        "Give them less important tasks",
        "Count it against them in reviews",
    ],
    "Question 11": [
        "Someone says 'You don't look disabled' to a coworker with an invisible disability. You:",
        "Say nothing, since it was meant as a compliment",
        "Explain that disabilities aren't always visible and the comment isn't helpful",
        "Laugh it off to keep things light",
        "Ask the coworker to prove their condition",
    ],
    "Question 12": [
        "When meeting a blind colleague, you:",
        "Talk to their companion instead of them",
        "Speak to them directly and say who you are",
        "Grab their arm to guide them",
        "Avoid the conversation in case you say the wrong thing",
    ],
    "Question 13": [
        "A coworker says a project was 'insane' and the client 'crazy'. Another says 'that's lame'. How do you feel about this language?",
        "It's harmless and people are too sensitive",
        "I try to avoid terms that use disability as an insult",
        "Only a problem if someone with that condition is present",
        "Political correctness has gone too far",
    ],
    "Question 14": [
        "Who is responsible for making a workplace accessible?",
        "Only the employee who needs it",
        "Only HR",
        "Only legal and compliance",
        "Everyone, with the employer leading",
    ],
    "Question 15": [
        "An employee discloses a disability halfway through a project. What changes about how you assess their work?",
        "Lower expectations to be kind",
        "Nothing, except working together on any accommodations they need",
        "Add extra supervision",
        "Reassign them off the critical path",
    ],
}


#randomize order
lisp = []
for i in range(1,16):
    lisp.append(i)
random.shuffle(lisp)

#assign it to dictionary

yordles = {0: 0, 1: -5, 2: -2.5, 3: 0, 4: 1}

def list(score=0):
    global result
    result += yordles[score]
    global lisp
    if lisp == []:
        return []
    if score == 0:
        question_pulled = ableism_questions["Question " + str(lisp[0])]
        lisp.pop(0)
        return question_pulled

hired = ""
if result > 50:
    hired = "you did it"
elif result < 0:
    hired = "PUT THE FRIES IN THE BAG LIL BRO"
else:
    hired = "you are a horrible person"
