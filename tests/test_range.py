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
        with self.assertRaises(ValueError): # Must raise an exception
            Range(100, 10)