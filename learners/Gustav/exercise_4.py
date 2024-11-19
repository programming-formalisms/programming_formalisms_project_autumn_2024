def is_probability(x):
    """checks if the input is a probability"""
    return x >= 0 and x <=1

assert is_probability.__doc__
assert is_probability(0.5) == True