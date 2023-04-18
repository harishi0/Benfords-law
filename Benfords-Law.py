import os
salesData = input("type in the file to open")
correctFile = "sales.csv"

if salesData == correctFile:
    with open('sales.csv') as file:
        print(file.read())

    



