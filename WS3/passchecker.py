MIN_LEN=5
MAX_LEN=15

NUM_UPPER = 1
NUM_LOWER = 1
NUM_NUM = 1
SPECIAL_REQ = True
Special_values = "!@#$%^&*()_-=+'~,./'[]\<>?{}|"

passwordValid = False

while passwordValid == False:
    amountLower=0
    amountUpper=0
    amountSpec=0
    password=(input("Enter password: "))
    if (len(password) >= MIN_LEN) and (len(password) <= MAX_LEN):
        for character in password:
                if character.islower():
                    amountLower=amountLower+1
                if character.isupper():
                    amountUpper=amountUpper+1
                for value in Special_values:
                    if value==character:
                        amountSpec = amountSpec + 1
        if amountLower >= NUM_LOWER and amountUpper >= NUM_UPPER:
                if SPECIAL_REQ == True:
                    if amountSpec < 1:
                        print("Invalid, no special values")
                    else:
                        passwordValid = True
                else:
                        passwordValid = True
        else:
            print("Invalid password requires upper and lower characters")
    else:
        print("Invalid password, must be in character limit")
print("Password accepted")