


import tkinter as tk  
import jet     
import alexander
import christian
import raily
import random

easy_list = [alexander.PAE , christian.PCE , raily.PRE]
medium_list = [alexander.PAM]
hard_list = [alexander.PAH]

selected_dificulty = []

def easy_press():
    global selected_dificulty
    selected_dificulty = easy_list.copy()
    introduction.destroy()

def medium_press():
    global selected_dificulty
    selected_dificulty = medium_list.copy()
    introduction.destroy()

def hard_press():
    global selected_dificulty
    selected_dificulty = hard_list.copy()
    introduction.destroy()

introduction = tk.Tk()
introduction.title("Warden's Judgement")
introduction.geometry("800x400")

introduction_label = tk.Label(introduction, text = "This game will decide the fate of criminals that you will never see. There is limited information available. There may be a right answer, but you may not know until it is too late. Please choose a difficulty level and good luck on your first day of work as the warden", font=("Arial", 16), wraplength=700)
introduction_label.pack(pady=30)


easy_button = tk.Button(introduction, text="Easy", command=easy_press)
easy_button.pack()

my_spacer = tk.Label(introduction, text="")
my_spacer.pack()

medium_button = tk.Button(introduction, text="Medium", command=medium_press)
medium_button.pack()

my_spacer2 = tk.Label(introduction, text="")
my_spacer2.pack()

hard_button = tk.Button(introduction, text="Hard", command=hard_press)
hard_button.pack()

introduction.mainloop()
x = 0
while x < 3:
    decision = tk.Tk()

    random_index = random.randrange(len(selected_dificulty))    #randomly chooses one of our packed prompt variables

    random_prompt = selected_dificulty.pop(random_index)        #removes the randomly choosen variable to not get duplicates

    prompt, accepted, denied = random_prompt                    #unpacks the variables back into the 3 parts

    def approve_press():
        print("Approved!")
        decision.destroy()  
    
        approved_consequence = tk.Tk()
    
        approved_consequence.title("After Approval")
        approved_consequence.geometry("800x400") 
    
        approved_consequence_label = tk.Label(approved_consequence, text=accepted, font=("Arial", 16), wraplength=700)
        approved_consequence_label.pack(pady=30)
    
        continue_button = tk.Button(approved_consequence, text="Continue", command=approved_consequence.destroy)
        continue_button.pack()
    

    def denied_press():
        print("Denied!")  
        decision.destroy()  
    
        denied_consequence = tk.Tk()
    
        denied_consequence.title("After Denial")          
        denied_consequence.geometry("800x400")

        denied_consequence_label = tk.Label(denied_consequence, text=denied, font=("Arial", 16), wraplength=700) 
        denied_consequence_label.pack(pady=30)
    
        continue_button = tk.Button(denied_consequence, text="Continue", command=denied_consequence.destroy)
        continue_button.pack()


    decision.title("Will you allow an early release?")
    decision.geometry("1000x700") 

    decision_label = tk.Label(decision, text=prompt, font=("Arial", 16), wraplength=700)
    decision_label.pack(pady=30)


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
#4. Agree on vairables to ensure text is pulled properly into main loop.

#Things we individually need to do in our own files:
#1. Most importantly finalize the prompts for each of your prisorners one for each difficulty level, Easy, Medium, and Hard.
#2. Setting unique variables for all prompts, accepted consequences, and denied consequences.
#3. Create your own dictionary for your prompts using those unique variables and make sure it is formatted correctly to be pulled by the main.py file.

#Eventually we will want to make the game harder by restricting information about the prisoner or how they were arrested.
#Possibly only allowing the player to deny a certain amount of criminals due to budget constraints so the player will have to think about if there will be a worse criminal coming up.
#Try your best!

'''
looks like we will have to convert our dictionaries into 3 lists to randomly pull from
may have to use .pop to remove the used criminal from the pool after picked
'''