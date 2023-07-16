from manim import *
from neuron import *


class NeuronOutputComputation(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        neuron = Neuron(side_length=3, fill_opacity=0.7, fill_color=GREEN)
        self.add(neuron)
