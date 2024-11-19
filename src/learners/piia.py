def is_zero(x):
    '''
    determines if input is zero
    returns True if is zero
    returns False if not zero
    will raise exception if input is not an int
    '''
    if not isinstance(x, int):
        raise TypeError('x must be an int')
    if x == 0:
        return True
    elif x != 0:
        return False

assert is_zero.__doc__
assert not is_zero(0) == 42
assert is_zero(0) == True
assert is_zero(42) == False

has_thrown = False
try:
    is_zero('nonsense')
except:
    has_thrown = True
assert has_thrown