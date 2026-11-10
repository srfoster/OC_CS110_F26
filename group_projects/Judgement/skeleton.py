import tkinter as tk  #this seemed to work better for me than class example

decision1 = tk.Tk()

def approve_press():
    print("approved!")

def denied_press():
    print("denied!")

decision1.title("Will you allow an early release?")
decision1.geometry("800x400") # To make the window larger

#Planning to add the prompt here, but I don't know how to do that yet.

prompt = tk.Label( decision1, text = "criminal", wraplength = 700)
prompt.pack(pady =  30, padx = 30)

approved_button = tk.Button(decision1, text="Approved", command=approve_press,)
approved_button.pack()

my_spacer = tk.Label(decision1, text="")
my_spacer.pack()

denied_button = tk.Button(decision1, text="Denied", command=denied_press,)
denied_button.pack()



decision1.mainloop()