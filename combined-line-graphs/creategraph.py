from manim import *
import csv
from config import *

class GraphCreator():
    def CreateGraph(self, file, color, s_factor, plane):

        self.fillValues(file, s_factor)
        
        line_graph = plane.plot_line_graph(
            x_values = self.x_vals,
            y_values = self.y_vals,
            line_color = color,
            add_vertex_dots = show_dots,
            stroke_width = line_thickness,
            vertex_dot_style = dict(fill_color=dot_color),
            vertex_dot_radius = dot_radius
        )
        return line_graph

    
    def fillValues(self, file, s_factor):
        self.x_vals = []
        self.y_vals = []
        filepath = 'data/' + file
        with open(f'{filepath}', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                x, y = row
                self.x_vals.append(float(x))
                self.y_vals.append(float(y)*s_factor)
        
        self.sortValues()
        
        self.min_x = min(self.x_vals) - left_padding   * use_padding
        self.max_x = max(self.x_vals) + right_padding  * use_padding
        self.min_y = min(self.y_vals) - bottom_padding * use_padding
        self.max_y = max(self.y_vals) + top_padding    * use_padding
        
        if (not trim_to_range):
            self.min_x = min(0, self.min_x)
            self.min_y = min(0, self.min_y)
    
    def sortValues(self):
        pairs = sorted(zip(self.x_vals, self.y_vals), key=lambda pair: pair[0])
        self.x_vals = [x for x, _ in pairs]
        self.y_vals = [y for _, y in pairs] 