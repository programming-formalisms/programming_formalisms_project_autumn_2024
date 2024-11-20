def is_zero(number):
    """Testing if the number is zero."""
    if not isinstance(number, int):
        raise TypeError("'number' must be of type int.")
    if number == 0:
        return True
    return False

def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

assert isprime(7) == True
assert isprime(8) == False