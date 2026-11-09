from tkinter import *  #this seemed to work better for me than class example

decision1 = Tk()

def approve_press():
    print("Approved!")
    decision1.destroy()  # Close the window after approval
    approved_consequence = Tk()
    approved_consequence.title("After Approval")
    approved_consequence.geometry("800x400") #Need to add text after this
    continue_button = Button(approved_consequence, text="Continue", command=approved_consequence.destroy)
    continue_button.pack()
    

def denied_press():
    print("Denied!")  
    decision1.destroy()  # Close the window after denial
    denied_consequence = Tk()
    denied_consequence.title("After Denial")
    denied_consequence.geometry("800x400")
    continue_button = Button(denied_consequence, text="Continue", command=denied_consequence.destroy)
    continue_button.pack()

decision1.title("Will you allow an early release?")
decision1.geometry("800x400") # To make the window larger

decision1_label = Label(decision1, text="Will you allow an early release?", font=("Arial", 16), wraplength=700)
decision1_label.pack(pady=30)

#Planning to add the prompt here, but I don't know how to do that yet.
'''
prompt = Label(
    decision1,
    text = "criminal",
    font = ("Arial", 16),
    wraplength = 700
)
prompt.pack(pady =  30, padx = 30)
'''

approved_button = Button(decision1, text="Approved", command=approve_press,)
approved_button.pack()

my_spacer = Label(decision1, text="")
my_spacer.pack()

denied_button = Button(decision1, text="Denied", command=denied_press,)
denied_button.pack()



decision1.mainloop()
#End of first decision window.

#Wash Rinse and Repeat but change prompts and consequences for the second decision window.
decision2 = Tk()

def approve_press2():
    print("Approved!")
    decision2.destroy()


def denied_press2():
    print("Denied!")  
    decision2.destroy() 

decision2.title("Will you allow an early release?")
decision2.geometry("800x400")

approved_button2 = Button(decision2, text="Approved", command=approve_press2,)
approved_button2.pack()

my_spacer2 = Label(decision2, text="")
my_spacer2.pack()

denied_button2 = Button(decision2, text="Denied", command=denied_press2,)
denied_button2.pack()

decision2.mainloop()