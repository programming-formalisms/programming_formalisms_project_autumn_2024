#%% Exc 1
def is_zero(x):
    """Determines if input is zero.
    Args: integer 
    
    Return: bool True or False
    
    Returns error if input is not an integer
    """
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    if x == 0:
        return True
    return False

    
assert is_zero.__doc__
assert is_zero(0) == True
assert not is_zero(1)

has_thrown = False

try:
    is_zero('nonsense')
except:
    has_thrown=True
    
assert has_thrown

print(is_zero(0))

#%% Exc 2

def is_even(x):
    """
    Determine if the input is one integer that is even
    """
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
 
    return x % 2 == 0
    
assert is_even.__doc__
assert is_even(2)
assert not is_even(1)

has_thrown = False
try:
    is_even(0.0)
except TypeError:
    has_thrown = True
assert has_thrown

# %% Exc 3


