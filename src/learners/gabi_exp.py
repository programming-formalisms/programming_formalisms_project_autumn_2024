def is_odd(x):
    """Determine if `x` is odd.

    If `x` is not an integer number, a `TypeError` is raised.

    Returns `True` if `x` is odd
    """
    if not isinstance(x, int):
        msg = "'number' must be a number. Actual type of 'number': "
        raise TypeError(
            msg, type(x),
        )
    return not x % 2 == 0