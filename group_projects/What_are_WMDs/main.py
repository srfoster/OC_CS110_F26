#This will integrate everyone's module (hopefully).
while True:
    print("=" * 65)
    print("Welcome to the Weapons of Math Destruction Interactive Module!")
    print("=" * 65)
    print()
    print("Choose a topic:")
    print()
    print("1. Opacity")
    print("2. Scale")
    print("3. Damaging")
    print("4. Interactive Story")
    print("5. Test Your Knowledge")
    print()

    choice = input("Enter a number from 1 to 5: ")

    print()
    # change template file name to your file
    if choice == "1":
        import sylvester_opacity_module
    elif choice == "2":
        import file2
    elif choice == "3":
        import file3
    elif choice == "4":
        import file4
    elif choice == "5":
        import file5
    else:
        print("Invalid choice. Please run the program again and enter 1-5.")


"""
#maybe use gui for main module if we have time???
import tkinter as tk

clicks = 0

def on_click():
    global clicks
    clicks += 1
    print("Clicks = ", clicks)
#change click command to link to modules??

window = tk.Tk()
window.title("gui")

label = tk.Label(window, text="Welcome to the Weapons of Math Destruction Interactive Module!", font="Calibri, 20")
label.pack(pady=20)

button = tk.Button(window, text="Click Me!", command=on_click)
button.pack()
window.mainloop()
"""
