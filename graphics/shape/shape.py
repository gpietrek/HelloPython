from abc import ABC, abstractmethod

from graphics.base.point import Point
from graphics.plot.plot import Plot


class Shape(ABC):
    def __init__(self, pos: Point) -> None:
        if not isinstance(pos, Point):
            raise TypeError(f"pos can only be a Point")
        else:
            self._pos = pos

    def get_pos(self) -> Point:
        return self._pos

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def plot(self, plot: Plot) -> None:
        pass
