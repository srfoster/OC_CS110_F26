from tkinter import *
from tkinter import ttk
# Allows us to pass arguments for function calls in a button or other code that uses
# command=
# example: command=partial(on_send, "hello world")
from functools import partial
import math
import Nathan_morris as NM
import Lucas_Van_Wyhe_Criminals as Criminal
import Nathan_vonheeder as von

# sends the input in the input box to be tokenized in Nathan_morris
def on_send():
    NM.send_text(the_input.get())

# grabs the current tokens from Nathan_morris and stores it
tokens = NM.get_tokens()
new_criminal_text = Criminal.output_criminal()

def get_crime():
    new_criminal_text = Criminal.output_criminal()
    the_input.configure(text=new_criminal_text)

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

def on_slider_move(value):
    if tree.selection():
        selection = tree.selection()
        item_id = selection[0]
        val = tree.item(item_id, "values")
        val = val[0]
        fl = val[0]
        obj = tokens[fl][val]['weights'][0]
        int_val = float(value)
        MIN_LIMIT = -1.0
        MAX_LIMIT = 1.0
        raw_obj = obj + math.cos(int_val / 1.5) * 0.3
        obj = round(max(MIN_LIMIT, min(MAX_LIMIT, raw_obj)), 2)
        info_label.config(text=f"Object: {val} | Value: {obj}")
        tokens[fl][val]['weights'][0] = obj

def on_select(event):
    if tree.selection():
        selection = tree.selection()
        item_id = selection[0]
        val = tree.item(item_id, "values")
        val = val[0]
        fl = val[0]
        obj = tokens[fl][val]['weights'][0]
        info_label.config(text=f"Object: {val} | Value: {obj}")

# initilizes the GUI
root = Tk()
root.title("Prisoners of AI")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.6)
window_height = int(screen_height)
root.geometry(f"{window_width}x{window_height}")

# creates a the mainframe of the GUI
mainframe = ttk.Frame(root, padding=(3,3,12,12))
mainframe.grid(column=0, row=0, sticky=(N, W, E,S))

# creates the varible for storing the text from the input field
the_input = StringVar()

input_frame = ttk.Frame(mainframe)
input_frame.grid(column=0, row=1, columnspan=3, sticky=(W, E), padx=5, pady=10)
input_frame.columnconfigure(1, weight=1)

User_Label = ttk.Label(input_frame, text="User input:")
User_Label.grid(column=0, row=0, sticky=W, pady=10)
input_field = ttk.Entry(input_frame, textvariable=the_input)
input_field.grid(column=1, row=0, sticky=EW, padx=5, pady=10)

# configures the root of the gui for grids
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=10, pady=5)
input_field.focus()
root.bind("<Return>", on_send)

# creates the button send text that sends text in the input field to Nathan_morris
Send_Button = ttk.Button(input_frame, text="Send text", command=partial(on_send, the_input))
Send_Button.grid(column=2, row=0, sticky=W, pady=10)

# creates the button to refresh the treeview
Refresh_Button = ttk.Button(mainframe, text="Refresh token list", command=refresh)
Refresh_Button.grid(column=2, row=5, sticky=W)

# creates the button to generate a criminal from Lucas_Van_Wyhe_Criminals
Crime_Button = ttk.Button(mainframe, text="Generate Criminal", command=get_crime)
Crime_Button.grid(column=2, row=4)

Release_Button = ttk.Button(mainframe, text="Release?", command=partial(release, test))
Release_Button.grid(column=0, row=8, sticky=E, padx=10)

# creates the base of the treeview and starts each selection as the first key of the tokens
# in this case a-z
tree = ttk.Treeview(mainframe)
tree.heading('#0', text="Alphabet", anchor="w")
tree.column("#0", width=100, anchor="w")
tree.heading("Token", text="Token", anchor="center")
tree.column("Token", width=200, anchor="center")
for key, value in enumerate(tokens):
    tree.insert('', 'end', value, text=value)

tree.bind("<<TreeviewSelect>>", on_select)

# sets the location of the tree
tree.grid(column=0, row=5, sticky=(W), padx=10)

selection = tree.selection()
slider =ttk.Scale(mainframe, from_=0,to=100, orient="horizontal",length=200, command=on_slider_move)
slider.set(50)
slider.grid(column=1, row=6, sticky=W)

# creates several labels for the gui
Saved_Label = ttk.Label(mainframe, text="Saved Tokens")
Saved_Label.grid(column=0, row=3, sticky=(W, N), padx=10)
Released_Label = ttk.Label(mainframe, text="Pending prisoner information for release recommendation")
Released_Label.grid(column=1, row=8, sticky=W)
info_label = ttk.Label(mainframe, text="Object:")
info_label.grid(column=0, row=6, sticky=W, padx=10, pady=10)
#Generate_Criminal = ttk.Label(mainframe, text="Criminal").grid(column=3, row=3)

Networth = NetWorthFrame(mainframe)
Networth.grid(column=0, row=7, padx=10, pady=10, sticky=N)
# the mainloop for root
root.mainloop()
