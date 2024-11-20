def is_number(x):
    """
    gives True if x is int or float
    gives False otherwise
    """
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    elif len(x) > 1:
        raise TypeError("'x' must be a number")
    else:
        return False

assert is_number.__doc__
assert is_number(3.0) == True
assert is_number('nonsense') == False

has_thrown = False
try:
    is_number([1,2])
except:
    has_thrown = True

assert has_thrown