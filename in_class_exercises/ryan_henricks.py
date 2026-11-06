while True:
    string = input("enter something: or type BYE to exit: ")
    if string == "BYE":
        break
    for i in range(len(string)):
        print(string[-(i + 1)], end="")
    print()
