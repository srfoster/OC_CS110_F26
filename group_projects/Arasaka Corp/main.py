import marcus_grib as mg
import holden_zack as hz
import dj_peeples as dj
import tkinter as tk
import random

answer_set_1 = ["Very Good", "Good", "Bad", "Absolute Garbage"]
question_number = 0
window = tk.Tk()
window.title("Totally Not Sketchy Hiring Software")
question_label = "How are you today?"
answer_set = []

modules = {1:mg.list,
           2: dj.list,
           3: hz.list}

def answer_clicked(x):
    modules[x](x)
    rotator()

def module_decider():
           list = []
           while not list:
                      number = random.randint(1, 4)
                      list = modules[number]()
           return list

def rotator():
    global question_number
    global answer_set
    question_number += 1
    question_number_display.config(text=f"Question {question_number}")
    answer_set = module_decider()
    question_label_display.config(text=answer_set[0])
    for i in range(1, 5):
           answers[f"answer_{i}"].config(text=answer_set[i], command=lambda num = i: answer_clicked(num))

question_number_display = tk.Label(window, text="Question 0")
question_number_display.pack()
question_label_display = tk.Label(window, text=question_label)
question_label_display.pack()

answers = {}
for i in range(1, 5):
    answers[f"answer_{i}"] = tk.Button(window, text=answer_set_1[i - 1], command=rotator)
    answers[f"answer_{i}"].pack()

window.mainloop()
