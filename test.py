from manim import *

class Conv3DNetwork(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=135 * DEGREES)

        diag = VGroup()

        # Create layer1
        layer1_neurons = self.create_layer(BLUE_A)
        diag.add(layer1_neurons)
        self.show_layer(layer1_neurons, 0, IN*2)
        self.wait(0.5)

        # Create layer2
        layer2_neurons = self.create_layer(BLUE_B)
        diag.add(layer2_neurons)
        self.show_layer(layer2_neurons, 1, IN*2)
        self.wait(0.5)

        # Create layer3
        layer3_neurons = self.create_layer(BLUE_C)
        diag.add(layer3_neurons)
        self.show_layer(layer3_neurons, 2, IN*2)
        self.wait(0.5)

        # Create layer4
        layer4_neurons = self.create_layer(BLUE_D)
        diag.add(layer4_neurons)
        self.show_layer(layer4_neurons, 3, IN*2)
        self.wait(0.5)

        # Create layer5
        layer5_neurons = self.create_layer(RED_A)
        diag.add(layer5_neurons)
        self.show_layer(layer5_neurons, 4, IN*2)
        self.wait(0.5)

        #self.play(ApplyMethod(diag.rotate, 1.5), run_time=1.0)
        #self.wait(0.5)
        #self.play(ApplyMethod(diag.rotate, -1.5), run_time=1.0)

        #self.play(ApplyMethod(diag.rotate, 0.65, UR, run_time=2.0))

        #self.play(FadeOut(layer3_neurons))
        #self.play(FadeOut(layer2_neurons))

        #diag.remove(layer3_neurons)
        #diag.remove(layer2_neurons)

        #self.play(ApplyMethod(layer3_neurons.shift, IN), run_time=1.0)

        #self.play(ApplyMethod(diag.shift, IN*1.4), run_time=1.0)

        #self.play(ApplyMethod(diag.rotate, 0.25, UR, run_time=2.0))


    def create_layer(self, color: str) -> VGroup:
        layer_neurons = VGroup()
        layer_neurons.add(*[Prism(dimensions=[1, 1, 0.1]).set_fill(
            opacity=0.2).set_color(color) for _ in range(30)])
                
        layer_neurons.arrange_in_grid(rows=5, cols=6, buff=0)

        return layer_neurons
    
    def show_layer(self, layer: VGroup, layer_number: int, layer_position: np.ndarray) -> None :
        layer.shift(layer_position)
        self.play(FadeIn(layer))
        self.play(ApplyMethod(layer.shift, np.array(
            (-2.0, 2.0, 4.0)) - np.array((0.0, 0.0, layer_number * 0.1))), run_time=0.5)


class Conv3DNetwork2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=135 * DEGREES)

        sample = VGroup()

        # Create input layer
        column = VGroup()
        column.add(*[Prism(dimensions=[1, 1, 0.4]).set_fill(
            opacity=0.6) for _ in range(6)])
                
        column.arrange(RIGHT, 0.0)

        layer = VGroup()
        #layer.add(*[column.copy() for _ in range(5)])
        col1 = column.copy()
        col2 = column.copy()
        col3 = column.copy()
        col4 = column.copy()
        col5 = column.copy()

        layer.add(col1, col2, col3, col4, col5)
            
            
        layer.arrange(DOWN, 0.0)

        sample.add(layer)
        layer.shift(IN*2)
        self.play(FadeIn(layer))
        self.play(ApplyMethod(layer.shift, np.array(
            (-2.0, 2.0, 4.0)) - np.array((0.0, 0.0, 0 * 0.4))), run_time=0.5)

        self.wait(0.5)

        self.play(ApplyMethod(sample.rotate, 1.5), run_time=1.0)
        self.wait(0.5)
        self.play(ApplyMethod(sample.rotate, -1.5), run_time=1.0)

        self.play(ApplyMethod(sample.rotate, 0.65, UR, run_time=2.0))

class PositionTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=135 * DEGREES)


        neuron4 = Prism(dimensions=[1, 1, 0.3]).set_fill(opacity=0.6).set_color(BLUE)
        self.play(Create(neuron4))

        neuron1 = Prism(dimensions=[1, 1, 0.3]).set_fill(opacity=0.6).set_color(GREEN)
        neuron1.shift(RIGHT*3)
        self.play(Create(neuron1))

        neuron2 = Prism(dimensions=[1, 1, 0.3]).set_fill(opacity=0.6).set_color(RED)
        neuron2.shift(UP*3)
        self.play(Create(neuron2))

        neuron3 = Prism(dimensions=[1, 1, 0.3]).set_fill(opacity=0.6).set_color(ORANGE)
        neuron3.shift(IN)
        self.play(Create(neuron3))

class GroupTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=135 * DEGREES)
        boxes=VGroup(*[Prism(dimensions=[1, 1, 0.3]).set_fill(
                opacity=0.6) for _ in range(10)])
        boxes.arrange_in_grid(rows=2, cols=5, buff=0)
        self.add(boxes)
        self.play(FadeIn(boxes))

class Conv3DNetworkKEEP(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=135 * DEGREES)

        sample = VGroup()

        for i in range(3):
            # Create input layer
            column = VGroup()
            column.add(*[Prism(dimensions=[1, 1, 0.3]).set_fill(
                opacity=0.6) for _ in range(6)])
                
            column.arrange(RIGHT, 0.0)

            layer = VGroup()
            layer.add(*[column.copy() for _ in range(5)])

            layer.arrange(DOWN, 0.0)

            sample.add(layer)

            self.play(FadeIn(layer))
            self.play(ApplyMethod(layer.shift, np.array(
                (-2.0, 2.0, 2.0)) - np.array((0.0, 0.0, i * 0.2))), run_time=0.5)

        self.wait(0.5)

        self.play(ApplyMethod(sample.rotate, 1.5), run_time=1.0)
        self.wait(0.5)
        self.play(ApplyMethod(sample.rotate, -1.5), run_time=1.0)

        self.play(ApplyMethod(sample.rotate, 0.65, UR, run_time=2.0))