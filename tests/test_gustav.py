import unittest
from src.learners.is_prime import is_prime

class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(101))

if __name__ == "__main__":
    unittest.main()