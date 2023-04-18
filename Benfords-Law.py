import os
salesData = input("type in the file to open")
correctFile = "sales.csv"

if salesData == correctFile:
    folder = os.getcwd
    file = folder + "\\BENFORDS-LAW\\sales.csv"
    filename = open(file, "r")
    



