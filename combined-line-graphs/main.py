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
        
        self.x_label = plane.get_x_axis_label(
            Text(x_axis_label).scale(x_label_size),
            DOWN,
            3*DOWN,
        ).set_color(x_label_text_color)
        self.y_label = plane.get_y_axis_label(
            Text(y_axis_label).scale(y_label_size),
            UR,
            2*LEFT + 2*UP,
        ).set_color(y_label_text_color)
        
        graphs = GraphCreator().CreateGraphs(plane)
        
        if create_video:
            self.animateGraphs(plane, graphs)
        else:
            self.plotGraphs(plane, graphs)
        
    def animateGraphs(self, plane, graphs):
        
        self.play(Create(plane), run_time=2)
        
        if (show_labels):
            self.play(Create(self.y_label), run_time=1)
            self.play(Create(self.x_label), run_time=1)
        
        if not animate_individually:
            self.play(*graphs, run_time=video_duration)
        else:
            div_duration = video_duration/len(graphs)
            for graph in graphs:
                self.play(graph, run_time=div_duration)
    
    def plotGraphs(self, plane, graphs):
        if (show_labels):
            self.add(self.x_label)
            self.add(self.y_label)
        self.add(plane)
        self.add(*graphs)
