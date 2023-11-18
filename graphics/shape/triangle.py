from graphics.base.point import Point
from graphics.plot.plot import Plot
from graphics.shape.shape import Shape


class Triangle(Shape):

    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(
            Point(
                (p1.get_x() + p2.get_x() + p3.get_x()) / 3,
                (p1.get_y() + p2.get_y() + p3.get_y()) / 3
            )
        )
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._plot = Plot()

    def calculate_area(self) -> float:
        return (
                self._p1.get_x() * (self._p2.get_y() - self._p3.get_y())
                + self._p2.get_x() * (self._p3.get_y() - self._p1.get_y())
                + self._p3.get_x() * (self._p1.get_y() - self._p2.get_y())
        ) / 2

    def plot(self, plot: Plot) -> None:
        plot.plot_line(self._p1, self._p2)
        plot.plot_line(self._p2, self._p3)
        plot.plot_line(self._p3, self._p1)
