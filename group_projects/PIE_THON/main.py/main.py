import marcus_wilkerson
import matt_kaha
import diego_caskey

print("Welcome! Each of these loan approval models function differently. Try your luck with each one!")
print()
print("Choose a module:")
print("1) Module 1")
print("2) Module 2")
print("3) Module 3")

while True:
    print()
    choice = input("Enter a number: ")

    if choice == "1":
        marcus_wilkerson.run_module()
        break
    elif choice == "2":
        matt_kaha.run_module()
        break
    elif choice == "3":
        diego_caskey.run_module()
        break
    else:
        print("-> Please a valid response (1, 2, or 3)")
