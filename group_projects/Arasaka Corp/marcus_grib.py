import random
result = 0
racism_questions = [["What is your favorite color?", "Black", "Gray", "Red", "White"],
                    ["Insert the proper word into this sentence: '____, Racism is good'", "No", "Yes", "I don't know", "Maybe"]]
numbers = []
for i in range(0, 2):
    numbers.append(i)
random.shuffle(numbers)
def list(x=0):
    global numbers
    global result
    result += x
    if numbers == []:
        return []
    if x == 0:
        question_pulled = racism_questions[numbers[0]]
        numbers.pop(0)
        return question_pulled
