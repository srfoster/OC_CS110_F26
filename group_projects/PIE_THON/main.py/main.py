import marcus_wilkerson
import matt_kaha
import diego_caskey

print("Welcome! Each of these loan approval models function differently. Try your luck with each one!")
print()
print("Choose a module:")
print("1) Module 1")
print("2) Module 2")
print("3) Module 3")
print("4) Quit")

while True:
    print()
    choice = input("Select an option: ")

    if choice == "1":
        marcus_wilkerson.run_module()
    elif choice == "2":
        matt_kaha.run_module()
    elif choice == "3":
        diego_caskey.run_module()
    elif choice == "4":
        print()
        print("Thanks for playing!")
        break
    else:
        print("-> Please enter a valid response (1, 2, 3, or 4)")
