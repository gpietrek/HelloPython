from graphics.base.point import Point
from graphics.base.util import check_float_positive
from graphics.plot.plot import Plot
from graphics.shape.circle import Circle
from graphics.shape.rectangle import Rectangle


class Oval(Rectangle, Circle):

    def __init__(self, pos: Point, width: float, height: float) -> None:
        super(Oval, self).__init__(self, pos=pos, width=width, height=height, radius=height / 2)

    def calculate_area(self) -> float:
        return Rectangle.calculate_area(self) + Circle.calculate_area(self)

    def plot(self, plot: Plot, color: str = 'red') -> None:
        plot.plot_rectangle(self._p1, self._width, self._height, color)
        plot.plot_circle(Point(self._p1.get_x(), self.get_pos().get_y()), self._radius, color)
        plot.plot_circle(Point(self._p2.get_x(), self.get_pos().get_y()), self._radius, color)

    def __str__(self) -> str:
        return f"Oval({self.get_pos()},{self.get_width()},{self.get_height()})"
