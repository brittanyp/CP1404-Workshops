print('Temperature Conversion Program')

def validate_number(str):
    valid = False
    num = input(str)
    while valid == False:
        if num.strip('-').isnumeric():
            valid=True
        else:
            print("Enter valid number")
            num=input(str)

    return(num);

celsiusValue = float(validate_number('Enter Celsius Value'))
fahrenheitValue = celsiusValue * 9 / 5 + 32
kelvinValue = celsiusValue + 273.15

print('celsius value: ', celsiusValue)
print('fahrenheit value:', fahrenheitValue)
print('Kelvin value:', kelvinValue)