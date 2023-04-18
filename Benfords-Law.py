import os
def printfile():
    with open('sales.csv') as file:
        print(file.read())

salesData = input("type in the file to open")
correctFile = "sales.csv"

while salesData != correctFile:
    print("invalid file, try again!")
    salesData = input("type in the file to open")

printfile()

    



