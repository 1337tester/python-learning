import csv
import os

script_dir = os.path.abspath( os.path.dirname( __file__ ) )
filename = "gateways_20161124.csv"
filepath = os.path.join(script_dir, filename)

with open(filepath, newline = '') as file:
    reader = csv.reader(file)
    header = next(reader)
    data = [row for row in reader]
    print(header)
    print(data[0])
