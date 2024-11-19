import random

def create_test_bacterium():
    'Creates a single bacteria that hopefully will be moving and eating at the end of it all'
    # simulate x and y within certain coordinate limits
    #that will be our starting position of the bacterium

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    return {"x": x, "y": y}

assert create_test_bacterium.__doc__

def is_bacterium(bacterium):
    '''Check whether the bacterium has valid x and y coordinates as floats.'''
    return (
        "x" in bacterium and isinstance(bacterium["x"], float) and
        "y" in bacterium and isinstance(bacterium["y"], float)
    )

assert is_bacterium.__doc__

assert is_bacterium(create_test_bacterium()) == True
assert is_bacterium("nonsense") == False

