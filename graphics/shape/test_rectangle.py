from unittest import TestCase

from graphics.base.point import Point
from graphics.shape.rectangle import Rectangle


class TestRectangle(TestCase):

    def setUp(self):
        self.cut = Rectangle(Point(1,2), 3, 4)
    def test_get_width(self):
        # act
        result = self.cut.get_width()

        # assert
        self.assertEqual(4, result)

    def test_get_height(self):
        assert False

    def test_calculate_area(self):
        assert False

    def test_plot(self):
        assert False
