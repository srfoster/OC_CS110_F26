from tkinter import *
from tkinter import ttk
import Nathan_morris as NM

def on_send():
    NM.send_text(the_input.get())
    
root = Tk()
root.title("Prisoners of AI")

mainframe = ttk.Frame(root, padding=(3,3,12,12))
mainframe.grid(column=0, row=0, sticky=(N, W, E,S))

the_input = StringVar()
input_field = ttk.Entry(mainframe, width=7, textvariable=the_input)
input_field.grid(column=2, row=1, sticky=(W, E))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
input_field.focus()
root.bind("<Return>", send_text)

weight_one = StringVar()
ttk.Label(mainframe, textvariable=weight_one).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Send text", command=on_send).grid(column=3, row=1, sticky=W)

ttk.Label(mainframe, text="User input").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="AI weighted response").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="output").grid(column=3, row=3, sticky=W)

root.mainloop()
