def is_probability(x):
    """checks if the input is a probability"""
    if type(x) == int or type(x) == float:
        return x >= 0 and x <=1
    else:
        print('Input is not a number')
        return False

assert is_probability.__doc__
assert is_probability(0.5) == True
assert is_probability(1.5) == False
assert is_probability('iamstring') == False