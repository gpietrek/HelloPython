from graphics.base.point import Point
from graphics.plot.plot import Plot
from graphics.shape.circle import Circle
from graphics.shape.oval import Oval
from graphics.shape.rectangle import Rectangle
from graphics.shape.square import Square
from graphics.shape.triangle import Triangle


class Main:
    def run(self):
        plot = Plot()

        rectangle = Rectangle(16, 4, pos = Point(8,2))
        rectangle.plot(plot, 'hotpink')
        print(f"{rectangle} has area: {rectangle.calculate_area()}")

        triangle = Triangle(
            Point(0, 5),
            Point(16, 5),
            Point(0, 10)
        )
        triangle.plot(plot, 'mediumorchid')
        print(f"{triangle} has area: {triangle.calculate_area()}")

        square = Square(Point(3, 14), 6)
        square.plot(plot, 'magenta')
        print(f"{square} has area: {square.calculate_area()}")

        circle = Circle(3, pos=Point(12.5, 14))
        circle.plot(plot, 'thistle')
        print(f"{circle} has area: {circle.calculate_area()}")

        oval = Oval(Point(8, 20), 16, 4)
        oval.plot(plot)
        print(f"{oval} has area: {oval.calculate_area()}")

        plot.show()


if __name__ == '__main__':
    main = Main()
    main.run()
