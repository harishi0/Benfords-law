import os

#printing file data onto the terminal
def printfile():
    with open('sales.csv') as file:
        print(file.read())
    

salesData = input("type in the file to open")
correctFile = "sales.csv"

while salesData != correctFile:
    print("invalid file, try again!")
    salesData = input("type in the file to open")

printfile()

validate = input("press 2 to validate")
correctInp = "2"

def validateNumber():
    with open('sales.csv') as numbers:
        file = numbers.read()
        file = file.split()
    for i in file:
        DigitOne = i[4]
        print(DigitOne)


while validate != correctInp:
    validate = input("press 2 to validate")

validateNumber()
    



