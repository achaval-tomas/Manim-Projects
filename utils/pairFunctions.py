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

x_key = lambda pair : pair[0]
y_key = lambda pair : pair[1]

f = sorted(f, key=x_key)
g = sorted(g, key=x_key)
        
min_x = max(x_key(f[0]), x_key(g[0]))
max_x = min(x_key(f[-1]), x_key(g[-1]))

def avg(l):
    return round(sum(l)/len(l), 3)

output_filename = f_filename.split('.')[0] + '_vs_' + g_filename.split('.')[0] + '.csv'
step = round(1/precision, 3)

pairs = set()
x = min_x
while (x <= max_x):
    x = round(x, 3)
    
    f_x = [round(y_key(p), 3) for p in f if abs(x_key(p) - x) <= allowance]
    g_x = [round(y_key(p), 3) for p in g if abs(x_key(p) - x) <= allowance]
    
    if (f_x and g_x):
        pairs.add((avg(f_x)*f_scale_factor, avg(g_x)*g_scale_factor))
        
    x += step

pairs = sorted(pairs, key=x_key)
with open(f"{output_filename}", 'w') as file:
    for p in pairs:
        file.write(f"{x_key(p)}, {y_key(p)}\n")