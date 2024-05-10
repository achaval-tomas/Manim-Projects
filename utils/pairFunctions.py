# Aim: given two files of "x, f(x)" and "x, g(x)" values,
# pair them up to a single file filled with "f(x), g(x)" values.
#
# Use-Case: Two functions (f and g) depend on the time, and you wish to plot
# a graph of f vs g to compare their behaviours during a period of time.
import csv

# Select filenames
f_filename = 'example_f.csv'
g_filename = 'example_g.csv'

# OPTIONAL: scale the values of each function by this factor
f_scale_factor = 1
g_scale_factor = 1

# Set the precision (higher => more attempts to match points)
# 1 <= precision <= 10
precision = 5

# Maximum allowed displacement for a value of x
# "x, f(x)" -> "x +- allowance, f(x)"
allowance = 0.1

'''          DO NOT MODIFY BELOW THIS LINE             '''

# Returns a list of (x, y) values from a file representing a function
def file_to_list(filename):
    l = []
    with open(f'{filename}', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x, y = row
            l.append((float(x), float(y)))
    return l
                
f = file_to_list(f_filename)
g = file_to_list(g_filename)

# Keys to access x and y values of a pair (x, y)
x_key = lambda pair : pair[0]
y_key = lambda pair : pair[1]

# Sort the lists of pairs by their x-values
f = sorted(f, key=x_key)
g = sorted(g, key=x_key)

# Calculate the intersecting range of x-values for f and g
min_x = max(x_key(f[0]), x_key(g[0]))
max_x = min(x_key(f[-1]), x_key(g[-1]))

# Returns the average of a list, rounded to 3 decimal digits
def avg(l):
    return round(sum(l)/len(l), 3)

# Determines if x1 is within the allowed range around x2
def allowed(x1, x2):
    return abs(x1 - x2) <= allowance

# Returns a list of the y-values paired to the allowed x-values in p_list
def allowed_points(p_list, x):
    return [round(y_key(p), 3) for p in p_list if allowed(x_key(p), x)]

# The set "pairs" will contain a list of all (f(x), g(x)) pairs which were
# allowed to represent the same x-value.
# Example: Allowance is set to 0.2 and we iterate over the x-value of 15
# -> f containing (15.10, 20) allows f(15) ~ 20
# -> g containing (14.85, 55) allows g(15) ~ 55
# Then the pair "(f(15), g(15))" = (20, 55) will be added to the set.
pairs = set()
step = round(1/precision, 3)
x = min_x
while (x <= max_x):
    x = round(x, 3)
    
    f_x = allowed_points(f, x)
    g_x = allowed_points(g, x)
    
    if (f_x and g_x):
        pairs.add((avg(f_x)*f_scale_factor, avg(g_x)*g_scale_factor))
        
    x += step

pairs = sorted(pairs, key=x_key)
output_filename = f_filename.split('.')[0] + '_vs_' + g_filename.split('.')[0] + '.csv'
with open(f"{output_filename}", 'w') as file:
    for p in pairs:
        file.write(f"{x_key(p)}, {y_key(p)}\n")