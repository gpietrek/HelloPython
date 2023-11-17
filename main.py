from graphics.base.point import Point
from graphics.base.vector import Vector
from graphics.shape.rectangle import Rectangle
from graphics.shape.triangle import Triangle


class Main:
    def run(self):
        p = Point(1, 2)
        print(f"p: {p}")

        v = Vector(3, 4)
        print(f"v: {v}")

        print(f"p + v: {p + v}")
        print(f"v + v: {v + v}")

        r = Rectangle(p, 2, 4)
        r.plot()

        t = Triangle(
            Point(0, 0),
            Point(10, 0),
            Point(0, 5)
        )
        t.plot()


if __name__ == '__main__':
    main = Main()
    main.run()
