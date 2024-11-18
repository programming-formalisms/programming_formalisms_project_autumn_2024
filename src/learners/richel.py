def is_zero(x):
    """
    Determines if input is zero.
    
    Will return True if the input is an integer with value zero.
    Will return False if the input is an integer with a non-zero.
    Will raise an exception if the input type is not an integer
    """
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    return x == 0

assert is_zero.__doc__
assert is_zero(0) == True

# Must raise an exception if the input type is not an integer
has_thrown = False
try:
    is_zero("nonsense")
except:
    has_thrown = True
assert has_thrown