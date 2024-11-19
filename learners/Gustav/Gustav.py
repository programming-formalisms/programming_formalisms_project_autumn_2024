def is_even(x):
    """returns True if input is even
        otherwise returns False
    """
    if type(x) == int or type(x) == float:
        return x%2 == 0 
    else:
        return False

    
def is_zero(x):
    """returns True if input is zero
        otherwise returns False
    """
    return x == 0

def is_odd(x):
    """returns True if input is even
        otherwise returns False
    """
    if type(x) == int or type(x) == float:
        return x%2 != 0 
    else:
        return False

def is_probability(x):
    if type(x) == int or type(x) == float:
        return x >=0 and x <=1 
    else:
        return False
    
def is_prime(x):
    if type(x) == int or type(x) == float:
        if x == 0 or x == 1 or x == 2:
            return True
        else:
            for i in range(2,x):
                if (x % i) == 0:
                    return False
                else:
                    return True 
    else:
        return False            

assert is_even(1) == False   
assert is_even(0) == True   
assert is_even(31) == False   
assert is_even(2) == True
assert is_even("imastring") == False      

assert is_zero(1) == False   
assert is_zero(0) == True   
assert is_zero(31) == False   
assert is_zero(2) == False
assert is_zero("imastring") == False  

assert is_odd(1) == True
assert is_odd(0) == False
assert is_odd(31) == True
assert is_odd(2) == False 
assert is_odd("imastring") == False

assert is_probability(1) == True
assert is_probability(0) == True
assert is_probability(0.04) == True
assert is_probability("imastring") == False
assert is_probability(3.1) == False

assert is_prime(0) == True
assert is_prime(1) == True
assert is_prime(2) == True
assert is_prime(10) == False
assert is_prime(17) == True
assert is_prime(28) == False
assert is_prime("imastring") == False