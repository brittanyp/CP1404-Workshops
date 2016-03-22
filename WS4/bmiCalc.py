import math


def validate_number(str):
    valid = False
    num = input(str)
    while valid == False:

        if num.isdecimal():
            if int(num) > 0:
                valid=True
            else:
                print("Enter number in range")
                num=input(str)
        else:
            print("Enter valid number")
            num=input(str)

    return(num);

weight = float(validate_number("Enter Weight(kg): "))
height = float(validate_number("Enter Height(m): "))

bmi = float((weight / math.pow(height, 2)))

print('Your BMI value is: ',bmi)