
import tkinter as tk  
import jet     
import alexander
import christian
import raily
import random


#these are the font and background color variables for the various labels
backgroundColor = "#1a100e"
fontColor = "white"


#FUNCTION SECTION
def addInfo():
    #initialize copy list 
    #have list linked to the specific hard list 
    print("Hey I got here")
    return "hey I got here" #this is just placeholder

#TO DO :

#make this button work for the more information section on the hard mode
#hardAdditional = tk.Button(introduction ,text="I need some additional information",command=  jet.addInfo())




#PROMPT SECTION

PJH = (
    "NAME: Elena Vance\n"
    "AGE: 34\n"
    "HEIGHT: 5’5\n"
    "WEIGHT: 130 pounds\n"
    "EYES: Brown\n"
    "RACE: Hispanic\n"
    "GENDER: Female\n"
    "CRIMINAL RECORD: Elena was convicted of Cyber Espionage and Corporate Sabotage after leaking proprietary defense schematics to a foreign competitor.\n\n"
    "A burner phone hidden inside her intake folder vibrates with a single text: 'Approve her release, and the compromising photos from your last vacation disappear forever.'",
    "You approved her release. True to the message, the photos never surfaced—until six months later, when Elena vanished from the facility and federal agents traced the release authorization directly back to your terminal.",
    "You denied the transfer and turned the burner phone over to internal affairs. While the photos were leaked anonymously online, the resulting investigation uncovered a wider espionage ring, earning you a formal commendation."
)
prompt, accepted, denied = PJH

#add additional info here for variable


PJM = (
    "NAME: Marcus 'Doc' Mercer\n"
    "AGE: 52\n"
    "HEIGHT: 6’1\n"
    "WEIGHT: 210 pounds\n"
    "EYES: Blue\n"
    "RACE: Black\n"
    "GENDER: Male\n"
    "CRIMINAL RECORD: A former surgeon serving 15 years for running an illegal underground clinic that treated high-profile fugitives.\n\n"
    "Stapled to the back of his medical evaluation is a handwritten note: 'My daughter needs a rare heart procedure only I can perform. Grant me release, and I will owe you a life debt.'",
    "You granted his release. Marcus successfully performed the surgery at an undisclosed location. The media backlash cost you a promotion.",
    "You denied his request. Three weeks later, Marcus's daughter passed away while awaiting a specialist, and Marcus was placed on permanent suicide watch after attempting to take his own life in his cell."
)
prompt, accepted, denied = PJM


PJE = (
    "NAME: Arthur Pendelton\n"
    "AGE: 67\n"
    "HEIGHT: 5’10\n"
    "WEIGHT: 165 pounds\n"
    "EYES: Hazel\n"
    "RACE: White\n"
    "GENDER: Male\n"
    "CRIMINAL RECORD: Serving a 20-year sentence for Arson and Insurance Fraud after burning down his failing textile mill.\n\n"
    "Tucked inside his release application is a faded map of the county fairgrounds with a red X marked near the old bleachers, accompanied by a note: 'I know where the missing mayor is buried. Sign my release, and I’ll tell you.'",
    "You signed off on his release. Arthur led authorities to the exact spot on the map, finally bringing closure to a decade-old cold case—though the mayor's family publicly condemned you for letting a felon walk free.",
    "You denied his parole. Enraged, Arthur burned the map in front of the guards during his next yard period, taking the secret of the mayor's whereabouts with him when he suffered a fatal stroke two months later."
)
prompt, accepted, denied = PJE


