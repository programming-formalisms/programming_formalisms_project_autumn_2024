import unittest


def is_prime(x):
    """
    Determines the input number whether it is prime
    True for prime
    False for not prime
    Raise error for non-integer
    """
    if not isinstance(x, int) or x < 1:
        raise TypeError("Input must be a natural number")
    if x == 1:
        raise TypeError("Input must be a natural number greater than 1")
        return False  
    if x == 2:
        return True
    prime = lambda x: x > 1 and all(x % i for i in range(2, int(x**0.5) + 1))
    return prime(x)


class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(101))

if __name__ == "__main__":
    
    unittest.main()