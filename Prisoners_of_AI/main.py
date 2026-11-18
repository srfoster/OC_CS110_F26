from tkinter import *
from tkinter import ttk
import Nathan_morris as NM
import Lucas_Van_Wyhe_Criminals as Criminal
import Nathan_vonheeder as von

# sends the input in the input box to be tokenized in Nathan_morris
def on_send():
    NM.send_text(the_input.get())

# grabs the current tokens from Nathan_morris and stores it
tokens = NM.get_tokens()

# refreshes the tree view with any new tokens
def refresh():
    tokens = NM.get_tokens()
    for key in tokens:
        print(key)
        for ckey, cvalue in enumerate(tokens[key]):
            print(ckey, cvalue)
            child_iid = f"{key}::{ckey}"
            if tree.exists(child_iid):
                tree.item(child_iid, text=cvalue)
            else:
                
                tree.insert(
                    key,
                    "end",
                    iid=child_iid,
                    text=str(cvalue),
                    values=(str(cvalue),)
                )

# initilizes the GUI
root = Tk()
root.title("Prisoners of AI")

# creates a the mainframe of the GUI
mainframe = ttk.Frame(root, padding=(3,3,12,12))
mainframe.grid(column=0, row=0, sticky=(N, W, E,S))

# creates the varible for storing the text from the input field
the_input = StringVar()
input_field = ttk.Entry(mainframe, width=7, textvariable=the_input)
input_field.grid(column=2, row=1, sticky=(W, E))

# configures the root of the gui for grids
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
input_field.focus()
root.bind("<Return>", on_send)

weight_one = StringVar()
ttk.Label(mainframe, textvariable=weight_one).grid(column=2, row=2, sticky=(W, E))

# creates the button send text that sends text in the input field to Nathan_morris
ttk.Button(mainframe, text="Send text", command=on_send).grid(column=3, row=1, sticky=W)

# creates the button to refresh the treeview
ttk.Button(mainframe, text="Refresh token list", command=refresh).grid(column=3, row=5, sticky=W)

# creates the base of the treeview and starts each selection as the first key of the tokens
# in this case a-z
tree = ttk.Treeview(mainframe)
for key, value in enumerate(tokens):
    tree.insert('', 'end', value, text=value)

# sets the location of the tree
tree.grid(column=1, row=5)

# creates several labels for the gui
ttk.Label(mainframe, text="User input").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Saved Tokens").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="output").grid(column=3, row=3, sticky=W)

# the mainloop for root
root.mainloop()
