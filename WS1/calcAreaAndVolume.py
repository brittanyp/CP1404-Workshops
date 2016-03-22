print('Area Calculator')

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

width = int(validate_number('enter width: '))
height = int(validate_number('enter height: '))
depth = int(validate_number('enter depth: '))

area = width * height * depth

print(width, height, depth, area)