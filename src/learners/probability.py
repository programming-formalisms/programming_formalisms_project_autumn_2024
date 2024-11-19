def is_probability(x):
    """
    Determine if the input 'x' is in the range from 0 to 1.

    Returns True if x is in the range 0 to 1
    Returns False if x is outside that range
    Raise an exception when the input is not an integer
    """
    if not isinstance(x, float):
        raise TypeError("'x' must be of type float")    
    if (x>0.0) & (x<1.0):
        return True
    else:
        return False


assert is_probability.__doc__
assert is_probability(1) == True
assert is_probability(3) == False
#assert is_even(3) 

has_thrown = False
try:
    is_even(1.0)
except:
    has_thrown = True

assert has_thrown