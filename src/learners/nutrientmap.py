import numpy as np

def createmap(x, y):
    """
    gives 2d array of nutrient amonuts
    """
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")       
    if not isinstance(y, int):
        raise TypeError("'y' must be of type int")
    if (x<=0) or (y<=0):
        raise ValueError('x and y must be greater than 0')
    foodarray = np.zeros((x,y))
    sigma = 1
    xs = np.arange(x)
    ys = np.arange(y)
    for i in xs:
        for j in ys:
            G = 1 / (2*np.pi*sigma**2) * np.exp(-(i**2+j**2)/(2*sigma**2))
            foodarray[i,j] = G
    return(foodarray)

assert createmap.__doc__
food = createmap(4,5)
print(food)

has_thrown = False
try:
    createmap('lala','lolo')
    createmap(2)
except:
    hasthrown = True
assert hasthrown