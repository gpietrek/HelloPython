from graphics.base.point import Point
from graphics.plot.plot import Plot
from graphics.shape.shape import Shape


class Triangle(Shape):

    def __init__(self, p1: Point, p2: Point, p3: Point) -> None:
        if not isinstance(p1, Point):
            raise TypeError('p1 can only be a Point')
        if not isinstance(p2, Point):
            raise TypeError('p2 can only be a Point')
        if not isinstance(p3, Point):
            raise TypeError('p3 can only be a Point')
        super().__init__(
            Point(
                (p1.get_x() + p2.get_x() + p3.get_x()) / 3,
                (p1.get_y() + p2.get_y() + p3.get_y()) / 3
            )
        )
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

    def calculate_area(self) -> float:
        return (
                self._p1.get_x() * (self._p2.get_y() - self._p3.get_y())
                + self._p2.get_x() * (self._p3.get_y() - self._p1.get_y())
                + self._p3.get_x() * (self._p1.get_y() - self._p2.get_y())
        ) / 2

    def plot(self, plot: Plot, color: str = 'blue') -> None:
        plot.plot_triangle(self._p1, self._p2, self._p3, color)

    def __str__(self) -> str:
        return f"Triangle({self._p1},{self._p2},{self._p3})"
