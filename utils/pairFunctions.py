# Aim: given two files of "x, f(x)" and "x, g(x)" values,
# pair them up to a single file filled with "f(x), g(x)" values.
#
# Use-Case: Two functions (f and g) depend on the time, and you wish to plot
# a graph of f vs g to compare their behaviours during a period of time.
from copy import deepcopy
import csv

# Select filenames
f_filename = 'example_f.csv'
g_filename = 'example_g.csv'
output_filename = 'combined_functions.csv'

# OPTIONAL: scale the values of each function by this factor
f_scale_factor = 1
g_scale_factor = 1

# Set the precision (higher => more attempts to match points)
# 1 <= precision <= 10
precision = 5

# Maximum allowed displacement for a value of x
# "x, f(x)" -> "x +- allowance, f(x)"
allowance = 0.1

# Auxiliary function
def sortValues(x_vals, y_vals):
    pairs = sorted(zip(x_vals, y_vals), key=lambda pair: pair[0])
    x_vals = [x for x, _ in pairs]
    y_vals = [y for _, y in pairs]

f_x_vals = []
f_y_vals = []
with open(f'{f_filename}', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        x, y = row
        f_x_vals.append(float(x))
        f_y_vals.append(float(y))
                
g_x_vals = []
g_y_vals = []
with open(f'{g_filename}', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        x, y = row
        g_x_vals.append(float(x))
        g_y_vals.append(float(y))

sortValues(f_x_vals, f_y_vals)
sortValues(g_x_vals, g_y_vals)
        
min_x = max(f_x_vals[0], g_x_vals[0])
max_x = min(f_x_vals[-1], g_x_vals[-1])

f = zip(f_x_vals, f_y_vals)
g = zip(g_x_vals, g_y_vals)

def average(l):
    return round(sum(l)/len(l), 3)

step = round(1/precision, 3)
with open(f"{output_filename}", 'w') as file:
    x = min_x
    while (x <= max_x):
        x = round(x, 3)
        
        f_x = [round(y, 3) for z, y in deepcopy(f) if abs(z - x) <= allowance]
        g_x = [round(y, 3) for z, y in deepcopy(g) if abs(z - x) <= allowance]
        
        if (f_x and g_x):
            file.write(f"{average(f_x)*f_scale_factor}, {average(g_x)*g_scale_factor}\n")
            
        x += step