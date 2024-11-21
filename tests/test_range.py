import unittest

from src.learners.class_exercise import Range

class TestRange(unittest.TestCase):
    '''
    Tests the Range class
    '''
    def test_range(self):
        x = Range(3, 10)
        self.assertEquals(x.get_lowest(), 3)
        self.assertEquals(x.get_highest(), 10)
        self.assertRaises(ValueError, Range(100, 10)) # Must raise an exception
