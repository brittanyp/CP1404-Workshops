import math

choice = input(" (1) Even numbers.txt from x to y \n (2) Odd numbers.txt from x to y \n (3) Squares from x to y \n (4) Exit \n")

while choice !="4":
    x = int(input("Enter a start number: "))
    y = int(input("Enter an end number: "))
    if choice == "1":
       for i in range(x, y+1, 1):
            if i % 2 == 0:
                print(i)


    elif choice == "2":

        for i in range(x, y+1, 1):
            if i % 2 == 1:
                print(i)
    elif choice == "3":

        for i in range(x, y+1, 1):
            number=math.sqrt(i)
            if float(number).is_integer():
                print(i)


    else:
        print("Invalid Message")
    choice = input(" (1) Even numbers.txt from x to y \n (2) Odd numbers.txt from x to y \n (3) Squares from x to y \n (4) Exit \n")

print("You have quit")
