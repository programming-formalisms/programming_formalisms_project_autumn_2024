"""Tests all code in src.bacsim.piia_utils."""
import unittest

from src.bacsim.piia_utils import isprime

class TestPiiaUtils(unittest.TestCase):

    """Class to test the code in src.bacsim.piia_utils."""

    def test_isprime_responds_correctly_to_ints(self):
        """The function 'isprime' responds correctly to integers."""
        self.assertTrue(isprime(7))
        self.assertFalse(isprime(8))

    def test_isprime_raises_an_exception_upon_non_ints(self):
        """The function 'isprime' raises an exception upon non-ints."""
        self.assertRaises(TypeError, isprime, {1, 2})
        self.assertRaises(TypeError, isprime, "I am a string")