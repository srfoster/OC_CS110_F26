import marcus_grib as mg
import holden_zack
import dj_peeples 
import tkinter as tk
import random
import test

answer_set_1 = ["Very Good", "Good", "Neutral", "Bad", "Absolute Garbage"]
question_number = 0
var = "Hello"
window = tk.Tk()
window.title("Totally Not Sketchy Hiring Software")
question_label = tk.StringVar()
question_label.set("How are you today?")
answer_set = []



def answer_clicked(x):
    test.fun(x)
    rotator()

def module_decider():
     return ("Please Confirm", "Bad", "Very Bad", "Decent", "Good", "Very Good")

def rotator():
    global question_number
    global answer_set
    question_number += 1
    question_number_display.config(text=f"Question {question_number}")
    answer_set = module_decider()
    for i in range(1, 6):
        question_label_display.config(text=answer_set[0])
        answers[f"answer_{i}"].config(text=answer_set[i], command=lambda num = i: answer_clicked(num))

question_number_display = tk.Label(window, text="Question 0")
question_number_display.pack()
question_label_display = tk.Label(window, text=question_label.get())
question_label_display.pack()

answers = {}
for i in range(1, 6):
    answers[f"answer_{i}"] = tk.Button(window, text=answer_set_1[i - 1], command=rotator)
    answers[f"answer_{i}"].pack()

window.mainloop()
