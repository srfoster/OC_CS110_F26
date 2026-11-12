#print(jet.add(2,3))

'''
This above is how you pull functions from other modules
'''
import tkinter as tk  
import jet     #this is how you import other modules, in this case jet.py and we will have all our modules imported as well
import alexander
import raily
import christian


introduction = tk.Tk()
introduction.title("Warden's Judgement")
introduction.geometry("800x400") 

introduction_label = tk.Label(introduction, text = "This game will decide the fate of criminals that you will never see. There is limited information available. There may be a right answer, but you may not know until it is too late. Please choose a difficulty level and good luck on your first day of work as the warden", font=("Arial", 16), wraplength=700)
introduction_label.pack(pady=30)

#these buttons will pull randomly from the dictionaries of Easy, Medium, and Hard prompts in our code. 
easy_button = tk.Button(introduction, text="Easy", command=introduction.destroy)
easy_button.pack()

my_spacer = tk.Label(introduction, text="")
my_spacer.pack()

medium_button = tk.Button(introduction, text="Medium", command=introduction.destroy)
medium_button.pack()

my_spacer2 = tk.Label(introduction, text="")
my_spacer2.pack()

hard_button = tk.Button(introduction, text="Hard", command=introduction.destroy)
hard_button.pack()

introduction.mainloop()
x = 0
while x < 3:
    decision = tk.Tk()

    def approve_press():
        print("Approved!")
        decision.destroy()  
    
        approved_consequence = tk.Tk()
    
        approved_consequence.title("After Approval")
        approved_consequence.geometry("800x400") 
    
        approved_consequence_label = tk.Label(approved_consequence, text="import consequence", font=("Arial", 16), wraplength=700)
        approved_consequence_label.pack(pady=30)
    
        continue_button = tk.Button(approved_consequence, text="Continue", command=approved_consequence.destroy)
        continue_button.pack()
    

    def denied_press():
        print("Denied!")  
        decision.destroy()  
    
        denied_consequence = tk.Tk()
    
        denied_consequence.title("After Denial")         #below here is the import from jet.py 
        denied_consequence.geometry("800x400")

        denied_consequence_label = tk.Label(denied_consequence, text=jet.word(), font=("Arial", 16), wraplength=700) #example of importing from jet.py
        #denied_consequence_label = tk.Label(denied_consequence, text="Good choice, more evidence was found and they will be in prison for a long time.", font=("Arial", 16), wraplength=700)
        denied_consequence_label.pack(pady=30)
    
        continue_button = tk.Button(denied_consequence, text="Continue", command=denied_consequence.destroy)
        continue_button.pack()


    decision.title("Will you allow an early release?")
    decision.geometry("800x400") 

    decision1_label = tk.Label(decision, text="import prompt", font=("Arial", 16), wraplength=700)
    decision1_label.pack(pady=30)


    approved_button = tk.Button(decision, text="Approved", command=approve_press,)
    approved_button.pack()

    my_spacer = tk.Label(decision, text="")
    my_spacer.pack()

    denied_button = tk.Button(decision, text="Denied", command=denied_press,)
    denied_button.pack()

    decision.mainloop()
    x += 1
    
#After loop
conclusion = tk.Tk()

conclusion.title("Time to clock out")
conclusion.geometry("800x400")

conclusion_label = tk.Label(conclusion, text="You have made your decisions for the day, at this point you can only stand by your choices that they made the world a safer place.", font=("Arial", 16), wraplength=700)
conclusion_label.pack(pady=30)

conclusion_button = tk.Button(conclusion, text="Exit Game", command=conclusion.destroy)
conclusion_button.pack()

conclusion.mainloop()

#Things we will need to add in main.py:
#1. A dictionary to make it easier to pull our prompts randomly
#2. A function to throw the parts of the prompt pulled by the dictionary and place it in designated text boxes in the GUI.
#3. A funtion to pull from the different dictionaries based on the difficulty level chosen by the player.

#Things we individually need to do in our own files:
#1. Most importantly finalize the prompts for each of your prisorners one for each difficulty level, Easy, Medium, and Hard.
#2. Create your own dictionary for your prompts and make sure it is formatted correctly to be pulled by the main.py file.

#Eventually we will want to make the game harder by restricting information about the prisoner or how they were arrested.
#Possibly only allowing the player to deny a certain amount of criminals due to budget constraints so the player will have to think about if there will be a worse criminal coming up.