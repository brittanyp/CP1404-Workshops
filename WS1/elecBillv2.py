print('Electricity Bill Estimator V.2')

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
estimation = 1

while estimation == 1:
    tariffChoice = int(input("Which tariff do you use? 11 or 31? "))
    dailyUse=float(input("Please enter daily use in kWh: "))
    billDays=float(input("Please enter number of billing days: "))

    if tariffChoice == 11:
        estBill = TARIFF_11 * dailyUse * billDays
        print('Estimated Bill: $',"%.2f" % estBill)
        estimation = 0
    elif tariffChoice == 31:
        estBill = TARIFF_31 * dailyUse * billDays
        print('Estimated Bill: $', estBill)
        estimation = 0
    else:
        print("Invailed tariff")

