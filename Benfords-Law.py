import os
salesData = input("type in the file to open")
correctFile = "sales.csv"
def printfile():
    with open('sales.csv') as file:
        print(file.read())
if salesData == correctFile:
     printfile()
else:
    print("invalid file")

    



