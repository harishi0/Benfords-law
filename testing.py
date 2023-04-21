import matplotlib.pyplot as plt
import math
import os
# Define a function that extracts the first digit of a number
def first_digit(n):
    while n >= 10:
        n //= 10
    return n
# Load the sales data from the input file
filename = 'sales.csv'
if not os.path.exists(filename):
    print("File does not exist!")
    exit()
# Read the data from the CSV file
with open(filename, "r") as f:
    data = f.readlines()
# Extract the first digit of each sales value
first_digits = [first_digit(int(line.split(",")[1])) for line in data[1:]]
# Calculate the expected frequencies according to Benford's law
expected_freqs = [math.log10(1 + 1/d) for d in range(1, 10)]
# Calculate the percentages
actual_freqs = [first_digits.count(d) / len(first_digits) for d in range(1, 10)]

# Plot the expected and actual frequencies
plt.bar(range(1, 10), expected_freqs, color='b', alpha=1, label='Benford')
plt.bar(range(1, 10), actual_freqs, color='r', alpha=1, label='Actual')
plt.xlabel('First Digit')
plt.ylabel('Percentage')
plt.legend()
plt.show()