import tkinter as tk  
import jet
introduction = tk.Tk()
introduction.title("Warden's Judgement")
introduction.geometry("800x400") 

introduction_label = tk.Label(introduction, text = "This game will decide the fate of criminals that you will never see. There is limited information available. There may be a right answer, but you may not know until it is too late. Good luck on your first day of work as the warden", font=("Arial", 16), wraplength=700)
introduction_label.pack(pady=30)

introduction_button = tk.Button(introduction, text="Continue", command=introduction.destroy)
introduction_button.pack()

introduction.mainloop()

decision1 = tk.Tk()

def approve_press():
    print("Approved!")
    decision1.destroy()  # Close the window after approval
    
    approved_consequence = tk.Tk()
    
    approved_consequence.title("After Approval")
    approved_consequence.geometry("800x400") #Need to add text after this
    
    approved_consequence_label = tk.Label(approved_consequence, text="You shouldn't have done that, they killed more people.", font=("Arial", 16), wraplength=700)
    approved_consequence_label.pack(pady=30)
    
    continue_button = tk.Button(approved_consequence, text="Continue", command=approved_consequence.destroy)
    continue_button.pack()
    

def denied_press():
    print("Denied!")  
    decision1.destroy()  # Close the window after denial
    
    denied_consequence = tk.Tk()
    
    denied_consequence.title("After Denial") #balls
    denied_consequence.geometry("800x400")
    denied_consequence_label = tk.Label(denied_consequence, text=jet.word, font=("Arial", 16), wraplength=700)
    #denied_consequence_label = tk.Label(denied_consequence, text="Good choice, more evidence was found and they will be in prison for a long time.", font=("Arial", 16), wraplength=700)
    denied_consequence_label.pack(pady=30)
    
    continue_button = tk.Button(denied_consequence, text="Continue", command=denied_consequence.destroy)
    continue_button.pack()


decision1.title("Will you allow an early release?")
decision1.geometry("800x400") # To make the window larger

decision1_label = tk.Label(decision1, text="This criminal has committed a serious offense.", font=("Arial", 16), wraplength=700)
decision1_label.pack(pady=30)


approved_button = tk.Button(decision1, text="Approved", command=approve_press,)
approved_button.pack()

my_spacer = tk.Label(decision1, text="")
my_spacer.pack()

denied_button = tk.Button(decision1, text="Denied", command=denied_press,)
denied_button.pack()



decision1.mainloop()
#End of first decision window.

#Wash Rinse and Repeat but change prompts and consequences for the second decision window.
decision2 = tk.Tk()

def approve_press2():
    print("Approved!")
    
    decision2.destroy()


def denied_press2():
    print("Denied!")  
    
    decision2.destroy() 

decision2.title("Will you allow an early release?")
decision2.geometry("800x400")

decision2_label = tk.Label(decision2, text="This criminal may have been framed but they do not have an alibi.", font=("Arial", 16), wraplength=700)
decision2_label.pack(pady=30)

approved_button2 = tk.Button(decision2, text="Approved", command=approve_press2,)
approved_button2.pack()

my_spacer2 = tk.Label(decision2, text="")
my_spacer2.pack()

denied_button2 = tk.Button(decision2, text="Denied", command=denied_press2,)
denied_button2.pack()

decision2.mainloop()