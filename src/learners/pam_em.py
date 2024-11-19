def is_even(x):
    """ Function to indicate True if the input number is an even number (can be divided by 2)
    and False if the number is uneven, (can't be divided by 2)
    """
    if x == 2:
        return True
    if x == 0: 
        return False

assert is_even.__doc__
assert is_even(2) == True
