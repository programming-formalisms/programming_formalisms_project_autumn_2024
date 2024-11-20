def is_number(x):
    """Function that returns True if input is a number and False if it is not a number.
    Raises exception if input is not a number."""
    if  isinstance(x, float):
        return True
    elif isinstance(x, int):
        return True
    return False

assert is_number.__doc__
assert is_number(1.5) == True
assert is_number("string") == False
assert is_number(1) == True

