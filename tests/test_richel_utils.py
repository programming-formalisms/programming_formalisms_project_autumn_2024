"""Tests all code in src.bacsim.richel_utils."""
import unittest

from src.bacsim.richel_utils import is_zero
from src.bacsim.richel_utils import isprime

class TestRichelUtils(unittest.TestCase):

    """Class to test the code in src.bacsim.richel_utils."""

    def test_is_zero_has_documentation(self):
        """The function 'is_zero' has documentation."""
        self.assertTrue(is_zero.__doc__)
        self.assertIsNotNone(is_zero.__doc__)

    def test_is_zero_responds_correctly_to_ints(self):
        """The function 'is_zero' responds correctly to integers."""
        self.assertTrue(is_zero(0))
        self.assertFalse(is_zero(1))

    def test_is_zero_raises_an_exception_upon_non_ints(self):
        """The function 'is_zero' raises an exception upon non-ints."""
        self.assertRaises(TypeError, is_zero, {1, 2})
        self.assertRaises(TypeError, is_zero, "I am a string")

    def test_isprime(self):
        """The function 'isprime' is correct."""
        self.assertTrue(isprime(7))
        self.assertFalse(isprime(8))
        self.assertRaises(ValueError, isprime, -1)
