def is_gradient(x, y):
    """"
    Function that tests if both input numbers in the "create_gradient" 
    function actually form a gradient from lowest to highest.
    """
    if x < y:
        return True
    else:
        return False



assert is_gradient.__doc__
assert is_gradient("nonsense") == False
assert is_gradient(create_test_gradient()) == True
