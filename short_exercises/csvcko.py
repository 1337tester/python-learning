import csv
path = "gateways_20161124.csv"
file = open(path, newline = '')
reader = csv.reader(file)
header = next(reader)
data = [row for row in reader]

print(header)
print(data[0])
