from graphics.base.point import Point
from graphics.base.vector import Vector
from graphics.plot.plot import Plot
from graphics.shape.rectangle import Rectangle
from graphics.shape.square import Square
from graphics.shape.triangle import Triangle


class Main:
    def run(self):
        p = Point(1, 2)
        print(f"p: {p}")

        v = Vector(3, 4)
        print(f"v: {v}")

        print(f"p + v: {p + v}")
        print(f"v + v: {v + v}")

        plot = Plot()

        rectangle = Rectangle(p, 2, 4)
        rectangle.plot(plot)

        triangle = Triangle(
            Point(0, 5),
            Point(6, 5),
            Point(0, 10)
        )
        triangle.plot(plot)

        square = Square(Point(3, 14), 6)
        square.plot(plot)

        plot.show()


if __name__ == '__main__':
    main = Main()
    main.run()
