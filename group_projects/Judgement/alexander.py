from tkinter import *  #this seemed to work better for me than class example

decision1 = Tk()

def approve_press():
    print("Approved!")
    decision1.destroy()  # Close the window after approval

def denied_press():
    print("Denied!")  
    decision1.destroy()  # Close the window after denial

decision1.title("Will you allow an early release?")
decision1.geometry("400x200") # To make the window larger

my_label = Label(decision1, text="Please select an option:", font=("Arial", 14)) 
my_label.pack(pady=20)  #Can't see a change in the text

approved_button = Button(decision1, text="Approved", command=approve_press,)
approved_button.pack()

my_spacer = Label(decision1, text="")
my_spacer.pack()

denied_button = Button(decision1, text="Denied", command=denied_press,)
denied_button.pack()



decision1.mainloop()