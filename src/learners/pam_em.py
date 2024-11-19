def is_even(x):
    """ Function to indicate True if the input number is an even number (can be divided by 2)
    and False if the number is uneven, (can't be divided by 2)
    """
    if not isinstance(x, int):
        raise TypeError("the x must be an integer!")
    if x % 2 == 0:
        return True
    else:
        return False

assert is_even.__doc__
assert is_even(2) == True
assert is_even(0) == False
