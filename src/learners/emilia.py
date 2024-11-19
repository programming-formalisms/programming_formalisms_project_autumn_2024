def is_zero(x):
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    if x == 0:
        return True
    return False
