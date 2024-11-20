def check_is_number(x):
    """Determine if `x` is a number.

    If `x` is not a number, a `RuntimeError` is raised.

    Returns nothing.
    """
    if not is_number(x):
        msg = "'x' must be a number. "
        raise RuntimeError(
            msg,
            "Actual value of 'x': ", x,
        )

def is_number(x):
    """Determine if `x` is one number.

    Determine if `x` is one number,
    for example, '42' or '3.14.

    Returns `True` if `x` is one number
    """
    return isinstance(x, (int, float) )

def is_probability(x):
    """Determine if `x` is a probability.

    Determine if `x` is a probability,
    i.e. a value between 0.0 and 1.0, including both 0.0 and 1.0.
    If `x` is not a floating point number, a `TypeError` is raised.

    Returns `True` if `x` is a probability
    """
    if not isinstance(x, float):
        msg = "'number' must be a floating point number. "
        raise TypeError(
            msg,
            "Actual type of 'number': ", type(x),
        )
    min_probability = 0.0
    max_probability = 1.0
    return x >= min_probability and x <= max_probability


def check_is_probability(x):
    """Determine if `x` is a probability.

    If `x` is not a probability, a `RuntimeError` is raised.

    Returns nothing.
    """
    check_is_number(x)
    if not is_probability(x):
        msg = "'x' must be a probability. "
        raise RuntimeError(
            msg,
            "Actual value of 'x': ", x,
        )
    
    
    

assert check_is_probability.__doc__
assert not check_is_probability(1.0)

has_thrown = False
try:
    assert check_is_probability('one')
except:
    has_thrown = True
assert has_thrown