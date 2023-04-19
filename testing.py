import os
import csv
import matplotlib.pyplot as plt

# Define a function to calculate the frequency of first digits
def first_digit_freq(data):
    freq = [0] * 9
    for num in data:
        first_digit = int(str(num)[0])
        freq[first_digit-1] += 1
    return freq

# Define a function to plot the frequency of first digits
def plot_freq(freq):
    digits = list(range(1, 10))
    plt.bar(digits, freq)
    plt.title("Distribution of First Digits")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.show()

# Define the filename to read from
sales_file = "sales.csv"

# Check if the file exists
while not os.path.isfile(sales_file):
    print("The file does not exist.")
    sales_file = input("Please enter a valid filename: ")

# Read the data from the file
with open(sales_file, "r") as file:
    reader = csv.reader(file, delimiter=",")
    next(reader)  # skip header
    data = [float(row[1]) for row in reader]

# Calculate the frequency of first digits
freq = first_digit_freq(data)

# Plot the frequency of first digits
plot_freq(freq)

# Calculate the expected frequency according to Benford's law
benford_freq = [sum(freq) * (1 / (i * 1.0)) for i in range(1, 10)]

# Calculate the percentage difference between observed and expected frequencies
perc_diff = [((freq[i] - benford_freq[i]) / benford_freq[i]) * 100 for i in range(9)]

# Check if the data is likely to be fraudulent based on Benford's law
if all(29 <= diff <= 32 for diff in perc_diff):
    print("The data is likely to be valid.")
else:
    print("The data may be fraudulent.")

# Write the frequency data to a CSV file
with open("results.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Digit", "Observed Frequency", "Expected Frequency", "% Difference"])
    for i in range(9):
        writer.writerow([i+1, freq[i], round(benford_freq[i], 2), round(perc_diff[i], 2)])
