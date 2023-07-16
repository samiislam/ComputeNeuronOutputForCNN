from manim import *
from colour import Color


class Neuron(VGroup):
    """A three-dimensional neuron.

    Parameters
    ----------
    side_length
        Length of each side of the :class:`Neuron`.
    fill_opacity
        The opacity of the :class:`Cube`, from 0 being fully transparent to 1 being
        fully opaque. Defaults to 0.75.
    fill_color
        The color of the :class:`Cube`.
    stroke_width
        The width of the stroke surrounding each face of the :class:`Cube`.

    Examples
    --------

    .. manim:: CubeExample
        :save_last_frame:

        class CubeExample(ThreeDScene):
            def construct(self):
                self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

                axes = ThreeDAxes()
                cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE)
                self.add(cube)
    """

    def __init__(
        self,
        width: float = 2,
        height: float = 2,
        depth: float = 2,
        fill_opacity: float = 0.75,
        fill_color: Color = BLUE,
        stroke_width: float = 0,
        **kwargs,
    ) -> None:
        self.width = width
        self.height = height
        self.depth = depth
        super().__init__(
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            stroke_width=stroke_width,
            **kwargs,
        )

    def generate_points(self) -> None:
        """Creates the sides of the :class:`Cube`."""
        for vect in IN, OUT:
            face = Rectangle(
                side_length=self.side_length,
                shade_in_3d=True,
            )
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))

            self.add(face)

        for vect in LEFT, RIGHT:
            face = Square(
                side_length=self.side_length,
                shade_in_3d=True,
            )
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))

        for vect in UP, DOWN:
            face = Square(
                side_length=self.side_length,
                shade_in_3d=True,
            )
            face.flip()
            face.shift(self.side_length * OUT / 2.0)
            face.apply_matrix(z_to_vector(vect))

    init_points = generate_points
