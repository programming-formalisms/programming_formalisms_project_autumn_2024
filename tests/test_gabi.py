import unittest

from src.learners.gabi_exp import is_odd

class TestGabi(unittest.TestCase):

    """Class to test the functions in src.learners.anneli"""

    def test_is_odd(self):
        """Test 'is_zero'."""
        self.assertIsNotNone(is_odd.__doc__)
        self.assertTrue(is_odd(0))
        self.assertFalse(is_odd(1))
        self.assertRaises(TypeError, is_odd, {1, 2})
        self.assertRaises(TypeError, is_odd, "I am a string")