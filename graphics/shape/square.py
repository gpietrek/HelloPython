from graphics.base.point import Point
from graphics.shape.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, pos: Point, width: float) -> None:
        super().__init__(pos, width, width)
