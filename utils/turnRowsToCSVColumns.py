# Converts a 2-Row text file to a 2-column CSV file.
# Run with python3 turnRowsToCSVColumns.py
from re import sub

# The text file must contain comma-separated
# values "x1, x2, ..." on each row.
# It may contain other non-numeric caracters
# which will be filtered out.
filepath = 'test-files/example.txt'

# Example use-case:
# content of text file (x and x^2)
# x=0, x=1, then 2, x=3,  x=4,  x=5,  x=6
# y=0, y=1,   y=4 ,   9, y=16, y=25, y=36
# content of output file
# 0, 0
# 1, 1
# 2, 4
# ...
# 6, 36

# Read the first 2 lines from the file
lines = []
with open(f"{filepath}", 'r') as file:
    lines.append(file.readline())
    lines.append(file.readline())

# Extract numeric content of each comma-separated element
x_vals = [sub(r"[^0-9.]", "", x) for x in lines[0].split(",")] 
y_vals = [sub(r"[^0-9.]", "", y) for y in lines[1].split(",")]

# Remove empty values (those that were comma-separated 
# in the file but didn't contain numeric characters)
x_vals = [x for x in x_vals if x != ""]
y_vals = [y for y in y_vals if y != ""] 

# Amount of valid (x, y) pairs
length = min(len(x_vals), len(y_vals))

# Create a new file and write rows as columns
filename = filepath.split('/')[-1].split(".")[0] or 'output'
with open(f"{filename}_converted.csv", 'w') as file:
    for i in range(length):
        file.write(f"{x_vals[i]}, {y_vals[i]}\n")