from math import isclose
from unittest import TestCase

from graphics.base.point import Point
from graphics.shape.circle import Circle


class TestCircle(TestCase):

    def setUp(self):
        self.center = Point(1, 2)
        self.cut = Circle(self.center, 3)

    def test_init_fails_for_wrong_radius_type(self):
        # arrange
        radius = 'I am a string'

        # act & assert
        with self.assertRaisesRegex(TypeError, 'radius can only be a float or int'):
            Circle(self.center, radius)

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
