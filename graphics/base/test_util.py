from unittest import TestCase

from graphics.base.util import check_float


class Test(TestCase):

    def test_check_float_accepts_int(self):
        # arrange
        value = 42

        # act
        result = check_float(value)

        # assert
        self.assertTrue(isinstance(result, float))
        self.assertEqual(42.0, result)

    def test_check_float_accepts_float(self):
        # arrange
        value = 4.2

        # act
        result = check_float(value)

        # assert
        self.assertTrue(isinstance(result, float))
        self.assertEqual(4.2, result)

    def test_check_value_fails_for_string(self):
        # arrange
        value = "I am a string"

        # act & assert
        with self.assertRaisesRegex(TypeError, 'coordinate can only be a float or int'):
            check_float(value, 'coordinate')
