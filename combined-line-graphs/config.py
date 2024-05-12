# LineGraph Configuration
from manim import *

''' REQUIRED PARAMETERS '''

# Filename (must exist in data folder) and the color to represent it.
# You can also scale the function of each file by any factor
filenames     = ['example1.csv', 'example2.csv', 'example3.csv']
colors        = [GOLD_E        , BLUE          , RED           ]
scale_factors = [50            , 4             , 1             ]

# Select a name for each axis and whether or not to display them.
# You can also use one as a title and the other one as a description.
x_axis_label = "Gold: Foo, Blue: Bar, Red: Baz"
y_axis_label = "Lorem Ipsum over Sit Amet"
show_labels  = True

# IMPORTANT: Select the range of x-values and y-values to be shown
# This will be used for the main plane and should contain all 
# possible values for all functions.
x_range = [0, 200]
y_range = [0, 220]

# Numbers to be labeled on each axis are 
# ... , -step*2, -step, step, step*2, ...
# for all values that fall within the axis' range.
x_axis_step = 50
y_axis_step = 50

# If trim_to_range is set to True, each axis will only show
# the range of values found in the file.
# Else, the graph will be drawn as usual, with both axis
# intersecting at the value of (0, 0).
trim_to_range = False

# Add some spare range around each axis to surround the graph.
# Select the padding values in the optional parameters below.
use_padding = True

''' OPTIONAL PARAMETERS '''

# Select a color for the axes' label text.
label_text_color = BLUE

# Select the display size of each axis.
x_axis_length = 12
y_axis_length = 6

# Select the thickness and color with which
# the main plotting line will be drawn.
line_thickness = 2
line_color     = GOLD_E

# If show_dots = True, a dot will be drawn at each (x,y) point.
# You can also select the dot's radius and color.
show_dots  = False
dot_radius = 0.015
dot_color  = WHITE

# Choose a color, width and opacity level for the plane's background lines.
# opacity = 0 means no lines will be drawn
background_lines_color   = BLUE
background_lines_width   = 1
background_lines_opacity = 0.5

# Allow some padding for the range of values shown in each direction.
# If padding is set to 0 for direction A, then the axis that moves in
# direction A will end at the farthest point in direction A from the file.
# Else, it will go to the farthest point + padding in that direction.
right_padding  = 1.5
left_padding   = 0
top_padding    = 3
bottom_padding = 0