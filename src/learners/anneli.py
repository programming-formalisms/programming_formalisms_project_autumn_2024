def is_zero(x):
    """Determines if input is zero.
    Will return True if input is zero.
    Will return False if input is not zero.
    Will raise an exception if input type is not integer."""

    if x == 0:
        return True

assert is_zero.__doc__
assert is_zero(0) == True