#You play as a person of color growing up in an impoverished neighborhood. You work at an office job on the brink of getting fired due to missing work on several occasions due to missing the bus
#Make the right choices and you can keep your job, but its more likely that youll lose your job and have to get another one, which will be difficult because you have a criminal record.
#Winning the game is only possible in one branch of desicions 
#game will track the amount of tries
def readsection(sect):
    for r in range(len(sect)):
        print(sect[r]) #This will automatically read lines and put them on new lines, which means sections are put into lists.

def gamestart(): #starts the game, resets any progress, and lets user return to the main file (in theory)
    progress = []
    print("Welcome to the interactive story!")
    print("A|Start")
    print("X|Exit back to main!")
    choice = input()
    if choice.upper = "A":

    elif choice.upper = "X":
        import main
        return_to_main()
  
