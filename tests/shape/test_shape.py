from unittest import TestCase

from graphics.base.point import Point
from graphics.shape.circle import Circle


# since Shape is abstract, we cannot test it directly, because we cannot instantiate it
# we use the concrete subclass Circle to test it
class TestShape(TestCase):

    def test_init_fails_for_wrong_pos_type(self):
        # arrange
        pos = 'I am a string'

        # act & assert
        with self.assertRaisesRegex(TypeError, 'pos can only be a Point'):
            Circle(pos, 3)

    def test_get_pos(self):
        # arrange
        cut = Circle(Point(1, 2), 3)

        # act
        result = cut.get_center()

        # assert
        self.assertEqual(Point(1, 2), result)
