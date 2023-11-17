from math import isclose
from unittest import TestCase

from graphics.base.point import Point
from graphics.shape.circle import Circle


class TestCircle(TestCase):

    def setUp(self):
        self.cut = Circle(Point(1,2), 3)

    def test_get_center(self):
        # act
        result = self.cut.get_center()

        # assert
        self.assertEqual(Point(1,2), result)

    def test_get_radius(self):
        # act
        result = self.cut.get_radius()

        # assert
        self.assertEqual(3, result)

    def test_calculate_area(self):
        # act
        result = self.cut.calculate_area()

        # assert
        self.assertTrue(isclose(28.274333882308139, result))

    def test_calculate_area_using_equal(self):
        # act
        result = self.cut.calculate_area()

        # assert
        self.assertEqual(28.274333882308139, result)
