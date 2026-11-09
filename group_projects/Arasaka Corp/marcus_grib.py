import tkinter as tk
window = tk.Tk()
window.title("Totally Not Sketchy Hiring Software")
question_number = tk.IntVar()
question_number.set("0")
def answer():
    question_number.set(question_number.get() + 1)
    label.config(text=f"Question {question_number.get()}")

label = (tk.Label(window, text="Question 0"))
label.pack()
tk.Button(window, text="Click me.", command=answer).pack()
window.mainloop()

