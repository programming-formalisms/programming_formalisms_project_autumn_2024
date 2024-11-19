def is_zero(x):
    """
    Determines the input number whether it is zero
    """
    if not isinstance(x, int):
        raise TypeError("Input must be an integer.")
    return x == 0

assert is_zero.__doc__
assert is_zero(0) == True
assert not is_zero(1)

has_thrown = False
try: 
    is_zero("nonsense")
except TypeError:
    has_thrown = True
assert has_thrown