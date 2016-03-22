print('Temperature Conversion Program')

celsiusValue = float(input('Enter Celsius Value'))
fahrenheitValue = celsiusValue * 9 / 5 + 32
kelvinValue = celsiusValue + 273.15

print('celsius value: ', celsiusValue)
print('fahrenheit value:', fahrenheitValue)
print('Kelvin value:', kelvinValue)