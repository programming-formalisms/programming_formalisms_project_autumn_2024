def is_zero(x):
    """Determines if input is zero.
    Will return True if input is zero.
    Will return False if input is not zero.
    Will raise an exception if input type is not integer."""

    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    if x == 0:
        return True
    elif x != 0:
        return False



assert is_zero.__doc__
assert is_zero(0) == True

# must raise an exception if the input type is not an integer
has_thrown = False
try:
    is_zero("nonsense")
except:
    has_thrown = True
assert has_thrown

#test