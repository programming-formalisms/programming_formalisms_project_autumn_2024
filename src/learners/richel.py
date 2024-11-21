"""Richel's code."""

def get_name():
    """Get Richel's name, spelled correctly."""
    return "Richèl"

# From https://www.pythonpool.com/check-if-number-is-prime-in-python/
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True





class Range:
    def __init__(self, any_lowest, any_highest):
        assert any_lowest <= any_highest
        self._lowest = any_lowest
        self._highest = any_highest
    def get_lowest(self):
        return self._lowest
    def get_highest(self):
        return self._highest

x = Range(3, 10)
assert x.get_lowest() == 3
assert x.get_highest() == 10
Range(100, 10) # Must raise an exception
