def is_one(x):
    """
    Determine if the input 'x' is one.

    Returns True if x is 1
    Returns False if x is not 1
    Raise an exception when the input is not an integer
    """
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")    
    if x == 1:
        return True
    else:
        return False


assert is_one.__doc__
assert is_one(1) == True
assert is_one(2) == False


has_thrown = False
try:
    is_one(1.0)
except:
    has_thrown = True

assert has_thrown