def is_even(x):
    """
    Determine if the input 'x' is even.

    Returns True if x is even
    Returns False if x is not even
    Raise an exception when the input is not an integer
    """
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")    
    if x % 2 == 0:
        return True
    else:
        return False


assert is_even.__doc__
assert is_even(2) == True
assert is_even(1) == False
#assert is_even(3) 

has_thrown = False
try:
    is_even(1.0)
except:
    has_thrown = True

assert has_thrown