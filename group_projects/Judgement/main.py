
import tkinter as tk  
import jet     
import alexander
import christian
import raily
import joey
import random

easy_list = [alexander.PAE , christian.PCE , raily.PRE_1 , alexander.PAE2, jet.PJE , joey.PJE]
medium_list = [alexander.PAM, raily.PRM_1, raily.PRM_2 , jet.PJM , joey.PJM]
hard_list = [alexander.PAH, raily.PRH_1, raily.PRH_2 , jet.PJH ,joey.PJH]
# added my prompts to the lists JET

selected_dificulty = []

global bonus
bonus = 0

def spacer(): #this function is for the introduction spacers specifically JET
    my_spacer = tk.Label(introduction,text="")
    my_spacer.configure(bg= jet.backgroundColor)
    my_spacer.pack()
    return

def spacer2(): #this function is for the decision spacers specifically JET
    my_spacer = tk.Label(decision, text="")
    my_spacer.configure(bg= jet.backgroundColor)
    my_spacer.pack()


def easy_press():
    global selected_dificulty
    selected_dificulty = easy_list.copy()
    global denials_remaining
    denials_remaining = 3
    introduction.destroy()

def medium_press():
    global selected_dificulty
    selected_dificulty = medium_list.copy()
    global denials_remaining
    denials_remaining = 2
    introduction.destroy()

def hard_press():
    global selected_dificulty
    selected_dificulty = hard_list.copy()
    global bonus 
    bonus = 1
    global denials_remaining
    denials_remaining = 2
    introduction.destroy()

introduction = tk.Tk()
introduction.title("Warden's Judgement")
introduction.geometry("800x500")

introduction.configure(bg= jet.backgroundColor) # added a background color for the main window JET

"""
my_spacer = tk.Label(introduction,text="")
my_spacer.configure(bg= jet.backgroundColor)
my_spacer.pack()
"""
spacer() #cleaned up spacer so it can just be written as a function instead of multiple lines over and over. JET

introduction_title = tk.Label(introduction, text = "Warden's Judgement", font = ("Impact", 30), fg= "red", wraplength=700)
introduction_title.configure(bg= jet.backgroundColor) #added background color to match JET
introduction_title.pack()


introduction_label = tk.Label(introduction, text = "This game will decide the fate of criminals that you will never see. There is limited information available. There may be a right answer, but you may not know until it is too late. Please choose a difficulty level and good luck on your first day of work as the warden\n""\n"
                              "WARNING: Due to budget cuts in the prison, you may have less denials than you expect due to capacity.", font=("Arial", 16), fg= jet.fontColor, wraplength=700) #added font color so you can see it JET
introduction_label.configure(bg= jet.backgroundColor) #added background color to match JET
introduction_label.pack(pady=30)


easy_button = tk.Button(introduction, text="Easy", command=easy_press)
easy_button.pack()

spacer()

medium_button = tk.Button(introduction, text="Medium", command=medium_press)
medium_button.pack()

"""
my_spacer2 = tk.Label(introduction, text="")
my_spacer2.configure(bg= jet.backgroundColor)
my_spacer2.pack()

not sure why there's a spacer 2 maybe this was initially made for the decision section?
"""
spacer()

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
        approved_consequence.configure(bg= jet.backgroundColor)
        approved_consequence.geometry("800x400") 
    
        approved_consequence_label = tk.Label(approved_consequence, text=accepted, font=("Arial", 16),fg= jet.fontColor, wraplength=700)
        approved_consequence_label.configure(bg= jet.backgroundColor)
        approved_consequence_label.pack(pady=30)
    
        continue_button = tk.Button(approved_consequence, text="Continue", command=approved_consequence.destroy)
        continue_button.pack()
    

    def denied_press():
        print("Denied!")  
        decision.destroy()  
        
        global denials_remaining

        if denials_remaining <= 0:
            return
        
        denials_remaining -= 1

        denied_consequence = tk.Tk()
    
        denied_consequence.title("After Denial")    
        denied_consequence.configure(bg= jet.backgroundColor)      
        denied_consequence.geometry("800x400")

        denied_consequence_label = tk.Label(denied_consequence, text=denied, font=("Arial", 16),fg= jet.fontColor, wraplength=700) 
        denied_consequence_label.configure(bg= jet.backgroundColor)
        denied_consequence_label.pack(pady=30)
    
        continue_button = tk.Button(denied_consequence, text="Continue", command=denied_consequence.destroy)
        continue_button.pack()


    decision.title("Will you allow an early release?")
    decision.geometry("1000x700") 
    decision.configure(bg= jet.backgroundColor) #added background color JET

   
    decision_label = tk.Label(decision, text=prompt, font=("Arial", 14), fg= jet.fontColor, wraplength=700)
    decision_label.configure(bg= jet.backgroundColor)
    decision_label.pack(pady=30)
    
    question_label = tk.Label(decision, text = "Will you allow an early release?", font = ("Arial", 20), fg= jet.fontColor, wraplength=700)
    question_label.configure(bg= jet.backgroundColor)
    question_label.pack()

    #my_spacer = tk.Label(decision, text="")
    #my_spacer.pack()

    denials_label = tk.Label(decision, text = f"Denials Remaining: {denials_remaining}", font =("Arial",16), fg= jet.fontColor, wraplength=700)
    denials_label.configure(bg= jet.backgroundColor)
    denials_label.pack()

    """
    my_spacer = tk.Label(decision, text="")
    my_spacer.pack()
    moved this into a function far up above
    """
    spacer2()

    approved_button = tk.Button(decision, text="Approved", command=approve_press,)
    approved_button.pack()

    spacer2()

    denied_button = tk.Button(decision, text="Denied", command=denied_press, state=tk.NORMAL if denials_remaining > 0 else tk.DISABLED)
    denied_button.pack()

    spacer2()

    if (bonus == 1):
        hard_additional = tk.Button(decision ,text="I need some additional information",command=  jet.addInfo())
        hard_additional.pack() # button for the additional info -- jet

    decision.mainloop()
    x += 1

#After loop
conclusion = tk.Tk()

conclusion.title("Time to clock out")
conclusion.configure(bg= jet.backgroundColor)
conclusion.geometry("800x400")

conclusion_label = tk.Label(conclusion, text="You have made your decisions for the day, at this point you can only stand by your choices that they made the world a safer place.", font=("Arial", 16), fg= jet.fontColor, wraplength=700)
conclusion_label.configure(bg= jet.backgroundColor)
conclusion_label.pack(pady=30)

conclusion_button = tk.Button(conclusion, text="Exit Game", command=conclusion.destroy)
conclusion_button.pack()

conclusion.mainloop()

#Things we will need to add in main.py:
#1. Agree on vairables to ensure text is pulled properly into main loop.

#Things we individually need to do in our own files:
#1. Most importantly finalize the prompts for each of your prisorners one for each difficulty level, Easy, Medium, and Hard.
#2. Setting unique variables for all prompts, accepted consequences, and denied consequences.
#3. Gonna make a function to have the font and background colors so we're not just piling main up and we can more easily change things to how we want

#Eventually we will want to make the game harder by restricting information about the prisoner or how they were arrested.
#Denying a certain prisoner may result in a prison riot which may result in the death of the warden
#possible weighted sums tied to the accepted or dinied prompts that are hidden until the end
#different endings based on the weighted sums

#different possible endings:
#SECOND-HAND MURDERER- letting out too many individuals that are clearly a public risk
#REFORMER- letting out the right prisoners the start a new life
#JUST CLOCKING IN- doing the bare minimum, not very bad but not very good
#LOCK DOWN- did not allow any prisoners early release


"""
Jet's Notes
I added my prompts to the lists after generating them with gemini to give me something then I editted the story SIGNIFICANTLY cause it really didn't understand the idea.
I also added background colors and font colors to the various windows, created a variable you can pull for the backgroundColor on my module that you can just throw into the () in <tklable>.configure() on anything you want)
Did the same for the text as well.
I want to go through and create variables for the fonts as well but I got too tired for that.

IN NO WAY AM I LIKE WE MUST HAVE THESE COLORS, I JUST PICKED SOMETHING FOR THE VARIABLES AND HOW THEY COULD GO IN.
If you wanna change the colors checkout my module for the fontColors and backgroundColors variables an play with it.
I also filled out the README.md file 
Please put some more that you guys would like to see in the readme
"""

