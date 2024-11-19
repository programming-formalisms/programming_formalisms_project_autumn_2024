
def is_zero():
    """
    Determines if the input is zero
     True = the input is an integer with zero value
     False = the input is an non-zero integer
     Exeception when the input type is not an integer
     
    """
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    if x == 0:
        return True
    return False

assert is_zero.__doc__
assert is_zero(0)
assert not is_zero(1)

has_thrown = False
try:
    is_zero("nonsense")
except TypeError:
    has_thrown = True
assert has_thrown