from graphics.base.point import Point
from graphics.base.util import check_float_positive
from graphics.plot.plot import Plot
from graphics.shape.shape import Shape


class Rectangle(Shape):

    def __init__(self, pos: Point, width: float, height: float) -> None:
        super().__init__(pos)
        self._width = check_float_positive(width, 'width')
        self._height = check_float_positive(height, 'height')
        self._p1 = Point(pos.get_x() - width / 2, pos.get_y() - height / 2)
        self._p2 = Point(pos.get_x() + width / 2, pos.get_y() - height / 2)
        self._p3 = Point(pos.get_x() + width / 2, pos.get_y() + height / 2)
        self._p4 = Point(pos.get_x() - width / 2, pos.get_y() + height / 2)

    def get_width(self) -> float:
        return self._width

    def get_height(self) -> float:
        return self._height

    def calculate_area(self) -> float:
        return self._width * self._height

    def plot(self, plot: Plot, color: str = 'green') -> None:
        plot.plot_rectangle(self._p1, self._width, self._height, color)

    def __str__(self) -> str:
        return f"Rectangle({self.get_pos()},{self.get_width()},{self.get_height()})"
