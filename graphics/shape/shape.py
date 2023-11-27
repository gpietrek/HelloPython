from abc import ABC, abstractmethod

from graphics.base.point import Point
from graphics.plot.plot import Plot


class Shape(ABC):
    def __init__(self, *, center: Point, **kwargs) -> None:
        if not isinstance(center, Point):
            raise TypeError('center can only be a Point')
        self._center = center

    def get_center(self) -> Point:
        return self._center

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def plot(self, plot: Plot) -> None:
        pass
