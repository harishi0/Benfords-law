import os
import math
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
    Calc_freq = [round(first_digits.count(digits) / len(first_digits)*100, 2) for digits in range(1, 10)]
    print(Calc_freq)    
    return Calc_freq

def Print_csv(data, filename):
    # write digit frequency data to CSV file
    with open(filename, 'w') as file:
        file.write('Digit,Frequency\n')
        for digi, freq in zip(range(1, 10), data):
            file.write(str(digi) + ' = ' + str(freq) + '\n')
    print(f'Digit frequency data written to {filename}.')

def file_percent():
    with open('results.csv','w') as results:
        results.write(str())

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

csv_print= input("type 3 to see results")
Correctinp_csv = "3"

while csv_print != Correctinp_csv:
    csv_print= input("incorrect input, type 3 to see results:") 

filename = "results.csv"
results = validateNumber()
Print_csv(results, filename)


'''
# Extract the first digit of each sales value
first_digits = [first_digit(int(line.split(",")[1])) for line in data[1:]]
# Calculate the expected frequencies according to Benford's law
expected_freqs = [math.log10(1 + 1/d) for d in range(1, 10)]
# Calculate the percentages
actual_freqs = [first_digits.count(d) / len(first_digits)*100 for d in range(1, 10)]
print(actual_freqs)
# Plot the expected and actual frequencies



type = input("type y to see digit frequency")

def filePercent():
    with open('results.csv','w') as results:
        results.write(str(actual_freqs))

while type != "y":
    type = input("type y to see digit frequency")

filePercent()
'''
