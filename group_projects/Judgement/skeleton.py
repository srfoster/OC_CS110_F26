import tkinter as tk 

#recommend putting an introduction window as well explaining the game and what the player is doing.

decision1 = tk.Tk()

def approve_press(): #function for if they press approve for an early release
    print("approved!")
    decision1.destroy() #destroyes the window after they press approved

    approved_aftermath = tk.Tk() # then you create a new window to display what happens after they press approved
    
    approved_aftermath.title("Enter title here")
    approved_aftermath.geometry("800x400") 
    
    approved_aftermath_label = tk.Label(approved_aftermath, text="Enter what happens after approval.", font=("Arial", 16), wraplength=700)
    approved_aftermath_label.pack(pady=30)
    
    aproved_aftermath_button = tk.Button(approved_aftermath, text="Continue", command=approved_aftermath.destroy)
    aproved_aftermath_button.pack()

def denied_press(): #function for if they press denied for an early release
    print("denied!")
    decision1.destroy()

    denied_aftermath = tk.Tk()

    denied_aftermath.title("Enter title here")
    denied_aftermath.geometry("800x400")

    denied_aftermath_label = tk.Label(denied_aftermath, text="Enter what happens after denial.", font=("Arial", 16), wraplength=700)
    denied_aftermath_label.pack(pady=30)
    
    denied_aftermath_button = tk.Button(denied_aftermath, text="Continue", command=denied_aftermath.destroy)
    denied_aftermath_button.pack()

decision1.title("Enter title here")
decision1.geometry("800x400") 

prompt = tk.Label( decision1, text = "Prompt with criminal information", wraplength = 700)
prompt.pack(pady =  30, padx = 30)

approved_button = tk.Button(decision1, text="Approved", command=approve_press,)
approved_button.pack()

my_spacer = tk.Label(decision1, text="")
my_spacer.pack()

denied_button = tk.Button(decision1, text="Denied", command=denied_press,)
denied_button.pack()



decision1.mainloop() #after this mainloop you would put another mainloop for another decision