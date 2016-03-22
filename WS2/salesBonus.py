#If sales < 1000, 10% bonus
#If sales >= 1000, bonues 15%

sales = float(input("Enter Sales: $"))

while sales > 0:
    if sales < 1000:
        bonus = sales* 0.1
    else:
        bonus = sales * 0.15

    print("Bonus is $:", bonus, sep='')

    sales = float(input("Enter Sales: $"))