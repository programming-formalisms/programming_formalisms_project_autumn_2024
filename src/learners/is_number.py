def is_number(x):
    """
    gives True if x is int or float
    gives False otherwise
    """
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True

assert is_number.__doc__
assert is_number(3.0) == True