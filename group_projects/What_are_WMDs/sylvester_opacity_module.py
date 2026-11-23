#maybe form full diagram from final at week 10 and distribute across weeks, either leave week 7 blank or put forming ideas in there

#WRITE TO A FILE AND OPEN WHEN USER TYPES OPTIONS?
#is .py in the filename or the file type? important for importing to main file





def run_code():

    #This program assumes the user has a basic understanding of python and an idea of what models are.
    
    import random
    
    #ansi codes for text designs
    italics = "\033[3m"
    bold = "\033[1m"
    underline = "\033[4m"
    reset = "\033[0m"
    line_up = "\033[1A"
    line_clear = "\x1b[2K"
    
    #list for options
    options = [f"1: Show me an example of opacity. ({underline}recommended to take first{reset})",
    "2: Why is opacity dangerous?",
    "3: How can opacity be avoided?",
    "4: Is all opacity bad?",
    "5: Exit the Opacity Module."
    ] #list, just write everything on the exam to be safe?? maybe not?
    
    #press enter to continue
    def next():
        input(f"{italics}\nPress Enter to continue.{reset}")
        print(line_up, line_clear, line_up)
    
    
    
    #option 1
    def opacity_example():
        print(f"\n{bold}Example Opaque Model{reset}")
        print("\nI have created a model that will rate your\ntrustworthiness from 1-100.")
        input("\nJust type your name: ") #did nothing with name, maybe say
        
        #defined function locally because it is only used in this part of the module
        def calculate_trustworthiness(): #random, trustworthy if >= 85, returns statement
            random_trust = random.randint(1,100)
            if random_trust < 85:
                trust_statement = "Your trustworthiness is " + str(random_trust) + "/100. You are untrustworthy."
            else:
                trust_statement = "Your trustworthiness is " + str(random_trust) + "/100. You are trustworthy."
            return random_trust, trust_statement
        
        rt, ts = calculate_trustworthiness()
        
        print("\n" + ts, "\nNow here's a question for you:")
        print("\nHow do you think the program came up with that number?\n")
        
        print("a. It did calculations based on the length of your name.")
        print("b. It looked your name up in public records.")
        print("c. Your trustworthiness score of", str(rt) + "/100 is a constant, same for everyone.\n")
        
        input("Answer: ")
        print("\nThe answer is actually none of these. Your trustworthiness score was")
        print("completely randomly generated, but you, the person the model evaluated,")
        print("didn't know that. That is opacity.")
        next()
    
    
    
    #option 2, edit for requirements and user interactiveness at the same time
    def opacity_danger():
        print(f"\n{bold}Danger of Opacity{reset}")
        print("\nOpacity is dangerous because the people that a model affects are unaware")
        print("of its decision making process, and are therefore unable to challenge its\ndecision.")
        next()
        print("The model in lesson 1 only deems you trustworthy if you received a score\nof 85 or larger.")
        next()
        print("85 is a pretty high minimum score, right? An opaque model wouldn't tell")
        print("you the minimum passing score or which factors make up your score. Opaque")
        print("models hide bias and human judgment in the form of math and code.")
        next()
    
    
    
    #option 3
    def opacity_prevent():
        print(f"\n{bold}Preventing Opacity{reset}")
        print("\nOpacity refers to a secretive decision making process and an inability for")
        print("people affected to appeal. Luckily, there are many ways for a developer to")
        print("prevent or reduce opacity.")
        next()
        print("One way is for the developer to have their program return a decision along")
        print('with an explanation.\ne.g. "Your trustworthiness score is below the 85/100 minimum."')
        next()
        print("Another way is for the developer to give users a way to ask questions about")
        print("their result or add an appeal option so that they can possibly get a\ndifferent result the same day.")
        next()
        print("In short, the harmful effects of opacity can be minimized if the developer")
        print("reveals parts of their model's decision making process or provides a way")
        print("for users to challenge the decision made.")
        next()
        
    
    
    #option 4
    def opacity_good():
        print(f"\n{bold}Good Opacity{reset}")
        print("\nNot all opacity is bad. A program that is opaque to the people it affects")
        print("is generally bad, but a program that is opaque to the programmers that")
        print("work on it is generally organized and easier to modify.")
        next()
        print("Sometimes, it's best that a model hides how it evaluates people in order")
        print("to avoid it being gamed. For instance, if a chef knows that they will be")
        print("evaluated based on the speed they can make dishes, they might sacrifice")
        print("quality for speed, but I'm sure most people would rather wait for a good")
        print("meal than get a bad one immediately.")
        next()
        #show parts of the code and bold and unbold them while talking about them
        #^^ do in part 3?
        
        
    
    #lesson check system
    def start_lesson(user_choice): #function with parameter
        if user_choice == "1": #this conditional concatenates a ✔ to the list above
            opacity_example() #to signify a completed lesson
            if "✔" not in options[int(user_choice) - 1]:
                options[int(user_choice) - 1] += " ✔"
        elif user_choice == "2":
            opacity_danger()
            if "✔" not in options[int(user_choice) - 1]:
                options[int(user_choice) - 1] += " ✔"
        elif user_choice == "3":
            opacity_prevent()
            if "✔" not in options[int(user_choice) - 1]:
                options[int(user_choice) - 1] += " ✔"
        elif user_choice == "4":
            opacity_good()
            if "✔" not in options[int(user_choice) - 1]:
                options[int(user_choice) - 1] += " ✔"
        elif user_choice == "5":
            print("\nThank you for using this program!\n") #maybe replace with link to other modules if not using
            return False # ^main.py as main thing to look at and instead are going through all of them one at a time
            # or just return to main.py
        else:
            print("\nInvalid Input.\n")
        return True
    
    
    
    #main code
    print("=" * 75)
    print("Opacity: When nobody that is affected by a model can see how it works.")
    print("=" * 75 + "\n")
    
    while True: #loop that keeps the program running
        print(f"{bold}What would you like to know about opacity?{reset}")
        for i in options: #loop that prints the user's options
            print(i)
            
        keep_going = start_lesson(input("Enter a number from 1 to 5: "))
        #^function with argument that runs lessons, almost always returns True, returns False when user chooses to exit
        #^boolean variable, almost always True, becomes False when the user chooses to exit
        if not keep_going: #conditional that exits the program when user chooses to
            break
    
    
    
    #remember requirements, finish coding in week 9, integration point on monday week 10, check requirements on same day
