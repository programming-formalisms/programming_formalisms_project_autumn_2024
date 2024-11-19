def is_zero(x):
    """
    Determines the input number whether it is zero
    """
    if not isinstance(x, int):
        raise TypeError("Input must be an integer.")
    return x == 0

def is_even(x):
    """
    Determines the input number whether it is even
    """
    if not isinstance(x, int):
        raise TypeError("Input must be an integer.")
    return x % 2 == 0

def is_odd(x):
    """
    Determines the input number whether it is odd
    """
    if not isinstance(x, int):
        raise TypeError("Input must be an integer.")
    return not is_even(x)

assert is_odd.__doc__
assert is_odd(3) == True
assert not is_odd(2)

has_thrown = False
try: 
    is_odd("nonsense")
except TypeError:
    has_thrown = True
assert has_thrown