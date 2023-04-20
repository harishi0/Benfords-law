import os
import math
# Check if the input file name matches the expected file name
correct_file = "sales.csv"
sales_data = input("Type in the file to open: ")
while sales_data != correct_file:
    print("Invalid file name. Please try again.")
    sales_data = input("Type in the file to open: ")

# Check if the file exists
if not os.path.isfile(sales_data):
    print
    
def load_sales_data(file_path):
    """
    This function loads the sales data from the input file and returns a list of dictionaries.
    Each dictionary represents a row in the input file, with keys based on the header.
    """
    with open(file_path, "r") as f:
        lines = f.readlines()
        header = lines[0].strip().split(",")
        expected_columns = ['date', 'customer_name', 'product_name', 'sales_amount']
        if header != expected_columns:
            print("Error: invalid format - missing or incorrect columns")
            exit()
        data = []
        for line in lines[1:]:
            values = line.strip().split(",")
            row = {header[i]: values[i] for i in range(len(header))}
            data.append(row)
    return data

def extract_first_digit(value):
    """
    This function extracts the first digit of a given value and returns it as an integer.
    If the value is not a number, returns None.
    """
    try:
        first_digit = int(str(value)[0])
        return first_digit
    except ValueError:
        return None

def calculate_frequency(data):
    """
    This function calculates the frequency of occurrence of the first digit of the sales_amount column.
    Returns a dictionary with keys from 1 to 9 and values representing the frequency.
    """
    freq = {d: 0 for d in range(1, 10)}
    for row in data:
        first_digit = extract_first_digit(row['sales_amount'])
        if first_digit is not None:
            freq[first_digit] += 1
    total = sum(freq.values())
    actual_freq = {k: v/total for k, v in freq.items()}
    return actual_freq

def calculate_expected_frequency():
    """
    This function calculates the expected frequency of occurrence of the first digit based on Benford's Law.
    Returns a dictionary with keys from 1 to 9 and values representing the expected frequency.
    """
    expected_freq = {d: math.log10(1 + 1/d) for d in range(1, 10)}
    return expected_freq

def detect_fraud(actual_freq, expected_freq, threshold=0.1):
    """
    This function compares the actual and expected frequencies and returns a list of indices
    where the difference between actual and expected frequencies is greater than the threshold.
    """
    diff = {k: actual_freq[k] - expected_freq[k] for k in expected_freq.keys()}
    fraud_indices = [k for k, v in diff.items() if abs(v) > threshold]
    return fraud_indices

def export_fraud_data(data, fraud_indices, file_name="fraud.csv"):
    """
    This function exports the rows in data with indices in fraud_indices to a file with the given name.
    """
    if len(fraud_indices) > 0:
        fraud_data = [data[i] for i in fraud_indices]
        with open(file_name, 'w') as f:
            f.write(",".join(data[0].keys()) + "\n")
            for row in fraud_data:
                f.write(",".join(row.values()) + "\n")

