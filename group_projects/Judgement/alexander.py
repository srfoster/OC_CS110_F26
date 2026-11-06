from tkinter import *

option = Tk()

def approve_press():
    print("Approved!")

def denied_press():
    print("Denied!")

option.title("Will you allow an early release?")
option.geometry("400x200")

my_label = Label(option, text="Please select an option:", font=("Arial", 14))
my_label.pack(pady=20)

approved_button = Button(option, text="Approved", command=approve_press, command=option.destroy)
approved_button.pack()

my_spacer = Label(option, text="")
my_spacer.pack()

denied_button = Button(option, text="Denied", command=denied_press, command=option.destroy)
denied_button.pack()



option.mainloop()