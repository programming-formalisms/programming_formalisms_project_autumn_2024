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