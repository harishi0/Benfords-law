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


def benfordslaw():
    pass

    
plt.plot(x, y, linewidth=2.0)

    




