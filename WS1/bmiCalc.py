import math

weight = float(input('Enter Weight(kg): '))
height = float(input('Enter Height(m): '))

bmi = float((weight / math.pow(height, 2)))

print('Your BMI value is: ',bmi)