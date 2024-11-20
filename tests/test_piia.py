import unittest

from src.learners.is_zero_pamella import is_zero

class TestSmall(unittest.TestCase):
    def test_raises(self):
        self.assertRaises(TypeError, is_zero, 'nonsense')
