from graphics.base.point import Point
from graphics.plot.plot import Plot
from graphics.shape.circle import Circle
from graphics.shape.rectangle import Rectangle
from graphics.shape.square import Square
from graphics.shape.triangle import Triangle


class Main:
    def run(self):
        plot = Plot()

        rectangle = Rectangle(Point(8, 2), 16, 4)
        rectangle.plot(plot, 'hotpink')

        triangle = Triangle(
            Point(0, 5),
            Point(16, 5),
            Point(0, 10)
        )
        triangle.plot(plot, 'mediumorchid')

        square = Square(Point(3, 14), 6)
        square.plot(plot, 'magenta')

        circle = Circle(Point(12.5, 14), 3)
        circle.plot(plot, 'thistle')

        plot.show()


if __name__ == '__main__':
    main = Main()
    main.run()
