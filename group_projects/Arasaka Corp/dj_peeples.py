import random

ableism_questions = {
    "Question 1": {
        "text": "A coworker asks for a screen-reader-friendly version of a document. What do you do?",
        "option_1": "Tell them it's too much extra work",
        "option_2": "Send it promptly and ask if anything else would help",
        "option_3": "Ask why they can't just use the regular version",
        "option_4": "Pass the request to HR and move on",
    },
    "Question 2": {
        "text": "Which best describes a workplace accommodation?",
        "option_1": "Special treatment for people who struggle",
        "option_2": "A burden on the rest of the team",
        "option_3": "A change or tool that lets someone do their job on equal footing",
        "option_4": "A favor granted at a manager's discretion",
    },
    "Question 3": {
        "text": "A teammate has regular medical appointments and a flexible schedule, but always delivers on time. You feel:",
        "option_1": "Annoyed, because it isn't fair to everyone else",
        "option_2": "Neutral, because the work gets done",
        "option_3": "Suspicious that they're taking advantage",
        "option_4": "Like they should have to prove they need it",
    },
    "Question 4": {
        "text": "A team event is planned at a venue with only stairs for access. A colleague uses a wheelchair. What do you do?",
        "option_1": "Suggest they just skip this one",
        "option_2": "Offer to carry them up",
        "option_3": "Raise it immediately and help find an accessible venue",
        "option_4": "Go ahead and ask them to let you know if it's a problem",
    },
    "Question 5": {
        "text": "A colleague privately tells you about their chronic illness. You:",
        "option_1": "Keep it confidential and treat them as you always have",
        "option_2": "Mention it to the team so everyone can 'be understanding'",
        "option_3": "Start giving them easier work without asking",
        "option_4": "Tell your manager in case it affects the project",
    },
    "Question 6": {
        "text": "Which phrase is most appropriate?",
        "option_1": "Suffers from a disability",
        "option_2": "Confined to a wheelchair",
        "option_3": "Handicapped person",
        "option_4": "Person with a disability",
    },
    "Question 7": {
        "text": "A candidate has a two-year employment gap due to a health condition. How should it affect your hiring decision?",
        "option_1": "It's a red flag about reliability",
        "option_2": "It shouldn't, and only their skills and fit matter",
        "option_3": "Only if the condition could return",
        "option_4": "Ask for medical details to be sure",
    },
    "Question 8": {
        "text": "You're hosting a video meeting and a Deaf colleague is attending. You:",
        "option_1": "Enable captions or arrange an interpreter beforehand",
        "option_2": "Wait for them to request it",
        "option_3": "Send notes afterward instead",
        "option_4": "Speak slowly and loudly",
    },
    "Question 9": {
        "text": "A neurodivergent teammate asks for instructions in writing rather than verbally. You:",
        "option_1": "Say everyone should be able to follow verbal instructions",
        "option_2": "Agree, but grumble about the extra effort",
        "option_3": "Agree and make it a team habit, since written is clearer for everyone",
        "option_4": "Tell them to ask a coworker to explain it",
    },
    "Question 10": {
        "text": "A colleague works at a different pace but their output is high quality. You:",
        "option_1": "Judge them by the quality of their results",
        "option_2": "Think they should speed up to match the team",
        "option_3": "Give them less important tasks",
        "option_4": "Count it against them in reviews",
    },
    "Question 11": {
        "text": "Someone says 'You don't look disabled' to a coworker with an invisible disability. You:",
        "option_1": "Say nothing, since it was meant as a compliment",
        "option_2": "Explain that disabilities aren't always visible and the comment isn't helpful",
        "option_3": "Laugh it off to keep things light",
        "option_4": "Ask the coworker to prove their condition",
    },
    "Question 12": {
        "text": "When meeting a blind colleague, you:",
        "option_1": "Talk to their companion instead of them",
        "option_2": "Speak to them directly and say who you are",
        "option_3": "Grab their arm to guide them",
        "option_4": "Avoid the conversation in case you say the wrong thing",
    },
    "Question 13": {
        "text": "A coworker says a project was 'insane' and the client 'crazy'. Another says 'that's lame'. How do you feel about this language?",
        "option_1": "It's harmless and people are too sensitive",
        "option_2": "I try to avoid terms that use disability as an insult",
        "option_3": "Only a problem if someone with that condition is present",
        "option_4": "Political correctness has gone too far",
    },
    "Question 14": {
        "text": "Who is responsible for making a workplace accessible?",
        "option_1": "Only the employee who needs it",
        "option_2": "Only HR",
        "option_3": "Only legal and compliance",
        "option_4": "Everyone, with the employer leading",
    },
    "Question 15": {
        "text": "An employee discloses a disability halfway through a project. What changes about how you assess their work?",
        "option_1": "Lower expectations to be kind",
        "option_2": "Nothing, except working together on any accommodations they need",
        "option_3": "Add extra supervision",
        "option_4": "Reassign them off the critical path",
    },
}

#get random number
rando_numb = random.randrange(1,16)

#assign it to dictionary
question_pulled = ableism_questions["Question " + str(rando_numb)]

#pull associated question
print(question_pulled)
