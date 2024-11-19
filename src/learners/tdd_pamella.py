def is_zero(number):
    """Testing if the number is zero."""
    if not isinstance(number, int):
        raise TypeError("'number' must be of type int.")
    if number == 0:
        return True
    return False

assert is_zero.__doc__

assert is_zero(0)
assert not is_zero(1)

has_thrown = False

try:
    is_zero("nonsense")
except:
    has_thrown = True
assert has_thrown