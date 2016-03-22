#1
outfile = open("name.txt", "w")

name=input("Enter your name: ")
print(outfile.write(name))
outfile.close()

#2
#infile = open("name.txt", "r")

#nameRead = infile.read().strip()
#print("Your name is ", nameRead)
#infile.close

in_file  =open("name.txt","r")
name  =  in_file.read().strip()
print("Your  name  is", name)
in_file.close()

#3
numfile = open('numbers.txt', "r")

number1 = int(numfile.readline())
number2 = int(numfile.readline())

print(number1 + number2)