# LineGraph Configuration
from manim import *

''' REQUIRED PARAMETERS '''

# Filename (must exist in data folder).
file = 'NodeTxQueueCaso1_0-1.csv'

# Select a name for each axis.
x_axis_label = "Simulation Time (sec)"
y_axis_label = "NodeTx Queue Size"

# Note: The range of values for each axis is automatically 
# chosen to fit the data.
# If you wish to customize it, check out the main file.

# Numbers to be labeled on each axis (within the range) are 
# ... , -step*2, -step, step, step*2, ...
x_axis_step = 20
y_axis_step = 5

''' OPTIONAL PARAMETERS '''

# Select a color for the axes' label text.
label_text_color = BLUE

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