import os
import matplotlib as plt
#printing file data onto the terminal
def printfile():
    with open('sales.csv') as file:
        print(file.read())
#firstdigit 
def first_digit(num):
    while num >= 10:
        num //= 10
    return num

def validateNumber():
    with open('sales.csv') as numbers:
        file = numbers.readlines()
    first_digits = [first_digit(int(line.split(",")[1])) for line in file[1:]]
    Calc_freq = [round(first_digits.count(digits) / len(first_digits)*100, 2,) for digits in range(1, 10)]
    return Calc_freq

#create the graph
def createGraph():
    digits = range(1, 10)
    freq = validateNumber()
    plt.bar(digits, freq)
    plt.xlabel('First Digit')
    plt.ylabel('Frequency (%)')
    plt.title('Benford\'s Law Distribution')
    plt.show()


def FraudCheck():
    First_digit_freq = validateNumber()
    if 29 <= First_digit_freq[0] <= 32:
        print("fraud did not occur, because first digit is between 29 and 32%")
    else:
        print("SALES FRAUD OCCURES YOU ARE A CRIMINAL")
    print(validateNumber())

def Print_csv(data, filename):
    # write digit frequency data to CSV file
    with open(filename, 'w') as file:
        file.write('Digit,Frequency\n')
        for digi, freq in zip(range(1, 10), data):
            file.write(str(digi) + ' = ' + str(freq) + '\n')
    print(f'Digit frequency writen to {filename}.')


salesData = input("type in the file to open:")
correctFile = "sales.csv"
 
while salesData != correctFile:
    print("invalid file, try again!")
    salesData = input("type in the file to open:") 

printfile()

validate = input("press 2 to validate:")
correctInp = "2"
 
while validate != correctInp:
    validate = input("press 2 to validate")

validateNumber()


FraudCheck()

csv_print= input("type 3 to see results")
Correctinp_csv = "3"

while csv_print != Correctinp_csv:
    csv_print= input("incorrect input, type 3 to see results:") 

filename = "results.csv"
results = validateNumber()
Print_csv(results, filename)



