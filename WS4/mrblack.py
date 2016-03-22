
lower = 10
upper = 100

def get_number(lower, upper):
    valid = False
    num=input("Enter a number ({}-{})".format(str(lower), str(upper)))
    while valid == False:
        if num.isdecimal():
            if int(num) > lower and int(num) < upper:
                valid=True
            else:
                print("Enter number in range")
                num=input("Enter a number ({}-{})".format(str(lower), str(upper)))
        else:
            print("Enter valid number")
            num=input("Enter a number ({}-{})".format(str(lower), str(upper)))

    return(num);

get_number(lower, upper)
for i in range(lower, upper, 11): # make sure we have integers of different 'length'
 print("{} {}".format(i, chr(i)))