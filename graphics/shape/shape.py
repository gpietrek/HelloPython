from abc import ABC, abstractmethod

from graphics.base.point import Point
from graphics.plot.plot import Plot


class Shape(ABC):
    def __init__(self, center: Point) -> None:
        if not isinstance(center, Point):
            raise TypeError('pos can only be a Point')
        self._pos = center

    def get_center(self) -> Point:
        return self._pos

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def plot(self, plot: Plot) -> None:
        pass
