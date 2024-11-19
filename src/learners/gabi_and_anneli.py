def is_odd(x):
    '''Function to check if a number is odd.
    Return True if the number is odd, False otherwise.
    Raises exception if input is not an integer'''

    if x % 2 != 0:
        return True

assert is_odd.__doc__
assert is_odd(1)
assert is_odd('one')
