from math import pi

from graphics.base.point import Point
from graphics.shape.shape import Shape


class Circle(Shape):

    def __init__(self, pos: Point, radius: float) -> None:
        super().__init__(pos)
        if not isinstance(radius, (int, float)):
            raise TypeError(f"radius can only be a float value")
        if radius <= 0:
            raise ValueError(f"radius must be larger than zero")
        self._radius = float(radius)

    def get_center(self) -> Point:
        return self.get_pos()

    def get_radius(self) -> float:
        return self._radius

    def calculate_area(self) -> float:
        return pi * self._radius ** 2