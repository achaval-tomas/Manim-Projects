# Aim: Create a file filled with "x, f(x)" points 
# for a given function f.

# Use-Case: To be plotted by csv-to-line-graph project.
# A 'function_name_points.csv' file will be generated.

# Precision (number of points to generate).
precision = 40

# Range (min and max values of x to apply the function to).
x_range = [-10, 10]

# Name and definition of the function.
# (function must be defined with the chosen name)
# You can use a function defined below, or add a new one.
func_name = "cubic"

'''                FUNCTION DEFINITIONS                 '''

# Add your own function here

def linear(x):
    return x

def cuadratic(x):
    return x*x

def cubic(x):
    return x**3

from math import sin
def sin_function(x):
    return sin(x)

'''            DO NOT MODIFY BELOW THIS LINE            '''

numbers_in_range = x_range[1] - x_range[0]
step = numbers_in_range/precision

chosen_func = globals()[f"{func_name}"]
with open(f"{func_name}_points.csv", "w") as file:
    x = x_range[0]
    while (x <= x_range[1]):
        file.write(f"{x}, {chosen_func(x)}\n")
        x += step        
