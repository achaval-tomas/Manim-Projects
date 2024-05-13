from manim import *
from config import *
from creategraph import *

class CombinedGraphs(Scene):
    
    def construct(self):
        
        plane = NumberPlane(
            x_range = (x_range[0], x_range[1], x_axis_step),
            y_range = (y_range[0], y_range[1], y_axis_step),
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
        ).set_color(x_label_text_color)
        y_label = plane.get_y_axis_label(
            Text(y_axis_label).scale(y_label_size),
            UR,
            2*LEFT + 2*UP,
        ).set_color(y_label_text_color)
        
        if (show_labels):
            self.add(x_label)
            self.add(y_label)
        
        self.add(plane)
        
        g = GraphCreator()
        for i in range(len(filenames)):
            linegraph = g.CreateGraph(filenames[i], colors[i], scale_factors[i], plane)
            self.add(linegraph)
        