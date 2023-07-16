from manim import *


class Conv3DNetwork(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=150 * DEGREES)

        for i in range(3):
            for j in range(5):
                # Create input layer
                layer = VGroup(*[Prism(dimensions=[1, 1, 0.2]).set_fill(
                    opacity=0.6) for _ in range(6)])
                layer.arrange(RIGHT, 0.0)

                self.play(Create(layer))
                self.play(ApplyMethod(layer.shift, np.array(
                    (0.0, 3.0, 2.0)) - np.array((0.0, j * 1.0, i * 0.2))), run_time=1)

        self.wait(1)
