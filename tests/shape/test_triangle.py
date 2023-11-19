from unittest import TestCase

from graphics.base.point import Point
from graphics.shape.triangle import Triangle


class TestTriangle(TestCase):

    def setUp(self):
        self.p1 = Point(0, 0)
        self.p2 = Point(9, 0)
        self.p3 = Point(0, 6)
        self.cut = Triangle(self.p1, self.p2, self.p3)

    def test_init_fails_for_wrong_p1_type(self):
        # arrange
        p1 = 'I am a string'

        # act & assert
        with self.assertRaisesRegex(TypeError, 'p1 can only be a Point'):
            Triangle(p1, self.p2, self.p3)

    def test_init_fails_for_wrong_p2_type(self):
        # arrange
        p2 = 'I am a string'

        # act & assert
        with self.assertRaisesRegex(TypeError, 'p2 can only be a Point'):
            Triangle(self.p1, p2, self.p3)

    def test_init_fails_for_wrong_p3_type(self):
        # arrange
        p3 = 'I am a string'

        # act & assert
        with self.assertRaisesRegex(TypeError, 'p3 can only be a Point'):
            Triangle(self.p1, self.p2, p3)

    def test_get_pos(self):
        # act
        result = self.cut.get_pos()

        # assert
        self.assertEqual(Point(3, 2), result)

    def test_calculate_area(self):
        # act
        result = self.cut.calculate_area()

        # assert
        self.assertEqual(27, result)
