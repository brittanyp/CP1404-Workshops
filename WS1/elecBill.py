print('Electricity Bill Estimator')

centsPerKwh=(float(input("Please enter cents/kWh: ")))/100
dailyUse=float(input("Please enter daily use in kWh: "))
billDays=float(input("Please enter number of billing days: "))

estBill = centsPerKwh * dailyUse * billDays

print('Estimated Bill: $',estBill)