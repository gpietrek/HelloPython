from unittest import TestCase

from graphics.base.point import Point
from graphics.shape.rectangle import Rectangle


class TestRectangle(TestCase):

    def setUp(self):
        self.pos = Point(1, 2)
        self.cut = Rectangle(self.pos, 3, 4)

    def test_init_fails_for_wrong_width_type(self):
        # arrange
        width = 'I am a string'
        height = 4

        # act & assert
        with self.assertRaisesRegex(TypeError, 'width can only be a float or int'):
            Rectangle(self.pos, width, height)

    def test_init_fails_for_negative_width(self):
        # arrange
        width = -3
        height = 4

        # act & assert
        with self.assertRaisesRegex(ValueError, 'width must be greater than zero'):
            Rectangle(self.pos, width, height)

    def test_init_fails_for_wrong_height_type(self):
        # arrange
        width = 3
        height = 'I am a string'

        # act & assert
        with self.assertRaisesRegex(TypeError, 'height can only be a float or int'):
            Rectangle(self.pos, width, height)

    def test_init_fails_for_negative_height(self):
        # arrange
        width = 3
        height = -4

        # act & assert
        with self.assertRaisesRegex(ValueError, 'height must be greater than zero'):
            Rectangle(self.pos, width, height)

    def test_get_width(self):
        # act
        result = self.cut.get_width()

        # assert
        self.assertEqual(3, result)

    def test_get_height(self):
        # act
        result = self.cut.get_height()

        # assert
        self.assertEqual(4, result)

    def test_calculate_area(self):
        # act
        result = self.cut.calculate_area()

        # assert
        self.assertEqual(12, result)