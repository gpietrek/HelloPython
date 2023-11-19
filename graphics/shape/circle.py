from math import pi

from graphics.base.point import Point
from graphics.base.util import check_float
from graphics.plot.plot import Plot
from graphics.shape.shape import Shape


class Circle(Shape):

    def __init__(self, pos: Point, radius: float) -> None:
        super().__init__(pos)
        self._radius = check_float(radius, 'radius')

    def get_center(self) -> Point:
        return self.get_pos()

    def get_radius(self) -> float:
        return self._radius

    def calculate_area(self) -> float:
        return pi * self._radius ** 2

    def plot(self, plot: Plot) -> None:
        plot.plot_line(self.get_center(), self.get_center())