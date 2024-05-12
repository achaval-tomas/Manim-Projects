from manim import *
from config import *
import csv

class CSVToLineGraph(Scene):
    
    def construct(self):
        self.fillValues()

        plane = NumberPlane(
            x_range = (self.min_x, self.max_x, x_axis_step),
            y_range = (self.min_y, self.max_y, y_axis_step),
            x_length = x_axis_length,
            y_length = y_axis_length,
            background_line_style = {
                "stroke_color": background_lines_color,
                "stroke_width": background_lines_width,
                "stroke_opacity": background_lines_opacity,
                },
            axis_config={
                "include_numbers": True,
                "include_ticks": True,
                },
            x_axis_config = {
                "label_direction":2*DOWN,
                },
            y_axis_config = {
                "label_direction":2*LEFT,
                },
        )
        plane.center()
        
        x_label = plane.get_x_axis_label(
            Text(x_axis_label).scale(x_label_size),
            DOWN,
            3*DOWN,
        ).set_color(label_text_color)
        y_label = plane.get_y_axis_label(
            Text(y_axis_label).scale(y_label_size),
            UR,
            2*LEFT + 2*UP,
        ).set_color(label_text_color)
        
        line_graph = plane.plot_line_graph(
            x_values = self.x_vals,
            y_values = self.y_vals,
            line_color = line_color,
            add_vertex_dots = show_dots,
            stroke_width = line_thickness,
            vertex_dot_style = dict(fill_color=dot_color),
            vertex_dot_radius = dot_radius
        )

        if (show_labels):
            self.add(x_label)
            self.add(y_label)
        self.add(plane, line_graph)
    
    def fillValues(self):
        self.x_vals = []
        self.y_vals = []
        filepath = 'data/' + file
        with open(f'{filepath}', 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                x, y = row
                self.x_vals.append(float(x))
                self.y_vals.append(float(y))
        
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
