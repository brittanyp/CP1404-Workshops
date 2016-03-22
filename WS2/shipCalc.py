quantity = int(input("Enter amount of item: "))
while quantity < 0 :
    print("Invalid input")
    quantity = int(input("Enter amount of item: "))

costPerItem = float(input("Enter shipping cost per item: "))

totalCharge = costPerItem * float(quantity)

if totalCharge > 100 :
    totalCharge = totalCharge - (0.1 * totalCharge)
print("Your shipping cost is: $%.2f" % totalCharge)