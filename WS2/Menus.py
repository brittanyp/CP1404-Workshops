name = input("Enter Name: ")

choice = (input(" (H)ello \n (G)oodbye \n (Q)uit \n")).upper()

while choice !="Q":
    if choice == "H":
        print("Hello ", name)
    elif choice == "G":
        print("Goodbye ", name)

    else:
        print("Invalid Message")
    choice = (input(" (H)ello \n (G)oodbye \n (Q)uit \n")).upper()
print("You have quit")
