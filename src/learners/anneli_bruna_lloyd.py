def is_number(x):
    """Function that returns True if input is a number and False if it is not a number.
    Raises exception if input is not a number."""
    if not isinstance(x, float):
        return False
    return True

assert is_number.__doc__
assert is_number(1.5) == True
assert is_number("string") == False