import random


lims = 100

def create_test_bacterium(lims):
    'Creates a single bacteria that hopefully will be moving and eating at the end of it all'
    # simulate x and y within certain coordinate limits
    #that will be our starting position of the bacterium
    x = random.randint(0, lims)
    y = random.randint(0, lims)
    
    
    
    
    
    return x, y, bacterium



assert create_test_bacterium.__doc__
assert x < lims
assert y < lims
assert is_bacterium(create_test_bacterium()) == True
assert is_bacterium("nonsense") == False