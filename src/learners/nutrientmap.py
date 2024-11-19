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
            xi = i - x/2
            yj = j - y/2
            G = 1 / (2*np.pi*sigma**2) * np.exp(-(xi**2+yj**2)/(2*sigma**2))
            foodarray[i,j] = G
    return(foodarray)

food = createmap(4,5)