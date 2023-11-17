import matplotlib.pyplot as plt

from graphics.base.point import Point


class Plot:

    def plot_line(self, p1: Point, p2: Point) -> None:
        plt.plot([p1.get_x(), p2.get_x()], [p1.get_y(), p2.get_y()])

    def show(self):
        plt.show()
