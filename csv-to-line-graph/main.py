from manim import *
from config import *
import csv

class CSVToLineGraph(Scene):
    
    def construct(self):
        self.fillValues()
        max_x = max(self.x_vals)
        max_y = max(self.y_vals)
        plane = NumberPlane(
            x_range = (0, max_x*1.01, x_axis_step),
            y_range = (0, max_y*1.20, y_axis_step),
            x_length = 12,
            y_length = 6,
            background_line_style = {
                "stroke_width": background_lines_width,
                "stroke_opacity": background_lines_opacity,
                },
            axis_config={
                "include_numbers": True,
                "include_ticks": True,
                },
            x_axis_config={"label_direction":2*DOWN},
            y_axis_config={"label_direction":2*LEFT},
        )
        plane.center()
        x_label = plane.get_x_axis_label(Text(x_axis_label).scale(0.45), DOWN, 3*DOWN).set_color(BLUE)
        y_label = plane.get_y_axis_label(Text(y_axis_label).scale(0.45), UR, 2*LEFT + 2*UP).set_color(BLUE)
        
        line_graph = plane.plot_line_graph(
            x_values = self.x_vals,
            y_values = self.y_vals,
            line_color=GOLD_E,
            add_vertex_dots=show_dots,
            stroke_width = line_width,
            vertex_dot_style=dict(fill_color=WHITE),
            vertex_dot_radius=dot_radius
        )

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
                x,y = row
                self.x_vals.append(float(x))
                self.y_vals.append(float(y))
        csvFile.close()
