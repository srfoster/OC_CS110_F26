import random

result = 0

sexist_questions = [
    [
        "A female coworker is promoted to lead a major client account, and a colleague comments that she probably got it because the client \"likes looking at her.\" How do you respond?",
        "a) Laugh it off to keep the peace",
        "b) Agree quietly, even if you aren't sure it's true",
        "c) Point out her qualifications and past wins on similar accounts",
        "d) Change the subject immediately",
    ],
    [
        "You are organizing a large client lunch and need someone to handle the catering order, room setup, and cleanup. Who do you ask?",
        "a) The most junior woman on the team, since she's naturally organized",
        "b) Whoever volunteers first",
        "c) Rotate the responsibility equally among all team members regardless of role or gender",
        "d) Ask the female administrative staff to handle it, even if it's outside their department",
    ],
    [
        "Two candidates—one man and one woman—have identical qualifications, except the woman has a two-year gap on her resume. What is your immediate assumption?",
        "a) She left the workforce to have or raise children",
        "b) She was probably laid off or struggled to find work",
        "c) Ask her directly about her background during the interview without assuming",
        "d) Pass on her resume in favor of the male candidate",
    ],
    [
        "During a brainstorming meeting, a woman suggests an idea that gets ignored. Ten minutes later, a man repeats the exact same idea and receives praise. What do you do?",
        "a) Nothing—the important thing is that the good idea is moving forward",
        "b) Speak up and credit her for bringing up the idea earlier",
        "c) Mention it to her privately after the meeting so she knows you noticed",
        "d) Assume the man explained it better and let him take the lead",
    ],
    [
        "A male coworker announces he is taking the full three months of paternity leave, while a female coworker announces she is taking three months of maternity leave. How do you view their commitment to the team?",
        "a) Both are equally entitled to their leave and remain equally committed",
        "b) The man is less committed because he doesn't physically need recovery time",
        "c) The woman is less committed because she will likely prioritize motherhood over work going forward",
        "d) Both are putting an unfair burden on the rest of the team",
    ],
    [
        "You notice a coworker getting visibly frustrated and raising their voice during a tense deadline. How do you interpret their behavior?",
        "a) It depends on whether it's a man or a woman—it's normal passion from a guy, but overly emotional from a woman",
        "b) They are stressed about the deadline and need support",
        "c) They are being unprofessional and need to calm down",
        "d) Ignore it unless it is directed at you",
    ],
    [
        "When building a shortlist for a high-travel, high-hours leadership role, you avoid nominating a qualified female colleague who recently got married. Why?",
        "a) You assume she will want to focus on starting a family soon",
        "b) You want to protect her work-life balance without asking her what she wants",
        "c) You shouldn't make that assumption—ask if she's interested in the opportunity",
        "d) You assume her spouse wouldn't approve of the travel schedule",
    ],
]

# Generates a random list of question
cat = []
for i in range(0, 7):
  cat.append(i)
random.shuffle(cat)

def get_next_question(x=0):
  global cat
  global result
  
  result += x
  
  if not cat:
    return []
  
  question_pulled = sexist_questions[cat[0]]
  cat.pop(0)
  
  return question_pulled
