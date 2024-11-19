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

assert is_even.__doc__
assert is_even(2) == True
assert not is_even(3)

has_thrown = False
try: 
    is_even("nonsense")
except TypeError:
    has_thrown = True
assert has_thrown
