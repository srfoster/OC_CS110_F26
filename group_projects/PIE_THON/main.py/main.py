import module1
import module2
import module3

print("Welcome! Each module is a loan approval model that makes its decision differently.")
print()
print("Choose a module:")
print("1) Module 1")
print("2) Module 2")
print("3) Module 3")

while True:
    print()
    choice = input("Enter a number: ")

    if choice == "1":
        module1.run_module()
        break
    elif choice == "2":
        module2.run_module()
        break
    elif choice == "3":
        module3.run_module()
        break
    else:
        print("-> Please enter 1, 2, or 3.")
