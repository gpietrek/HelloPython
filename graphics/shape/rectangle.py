from graphics.base.point import Point
from graphics.base.util import check_float
from graphics.plot.plot import Plot
from graphics.shape.shape import Shape


class Rectangle(Shape):

    def __init__(self, pos: Point, width: float, height: float) -> None:
        super().__init__(pos)
        self._width = check_float(width, 'width')
        self._height = check_float(width, 'height')
        self._p1 = Point(pos.get_x() - width / 2, pos.get_y() + height / 2)
        self._p2 = Point(pos.get_x() + width / 2, pos.get_y() + height / 2)
        self._p3 = Point(pos.get_x() + width / 2, pos.get_y() - height / 2)
        self._p4 = Point(pos.get_x() - width / 2, pos.get_y() - height / 2)

    def get_width(self) -> float:
        return self._width

    def get_height(self) -> float:
        return self._height

    def calculate_area(self) -> float:
        return self._width * self._height

    def plot(self, plot: Plot) -> None:
        plot.plot_line(self._p1, self._p2)
        plot.plot_line(self._p2, self._p3)
        plot.plot_line(self._p3, self._p4)
        plot.plot_line(self._p4, self._p1)
