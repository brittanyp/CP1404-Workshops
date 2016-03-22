try:
 numerator = int(input("Enter the numerator: "))
 denominator = int(input("Enter the denominator: "))
 fraction = numerator / denominator
except ValueError:
 print("Numerator and denominator must be valid numbers.txt!")
 #input is not valid
except ZeroDivisionError:
 #when denominator is 0
 print("Cannot divide by zero!")
print("Finished.")

#Q3 loop til valid denominator
