def is_zero(number):
    """Testing if the number is zero."""
    if not isinstance(number, int):
        raise TypeError("'number' must be of type int.")
    if number == 0:
        return True
    return False

# From https://www.pythonpool.com/check-if-number-is-prime-in-python/
def isprime(num):
    if not (num > 0):
        raise ValueError((f"Expected positive number. Received {num}."))
    if not isinstance(num, int):
        raise TypeError("'num' must be of type int.")
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
