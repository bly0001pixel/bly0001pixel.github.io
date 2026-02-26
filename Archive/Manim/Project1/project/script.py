from manim import *
import numpy as np

class GraphX(Scene):
    def construct(self):
        # Create axes with labels and range for both axes
        axes = Axes(
            x_range=[0, 8],  # x-axis range from 0 to 8
            y_range=[0, 8],  # y-axis range from 0 to 8
            axis_config={"color": BLUE},
        )

        # Set up the axis labels
        x_label = axes.get_axis_labels(x_label="$Gy$", y_label="$%$")

        # Define the function
        def func(x):
            return x  # Define a simple line y = x

        # Create the graph of the function
        graph = axes.plot(func, color=WHITE)

        # Display the axes, labels, and graph
        self.play(Create(axes), Write(x_label))
        self.play(ShowCreation(graph))

        self.wait(1)