
def is_zero(x):
    """
    Determines if the input is zero.
    
    - True: the input is an integer with a value of zero.
    - False: the input is a non-zero integer.
    - Raises a TypeError if the input is not an integer.
    """
    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    if x == 0:
        return True
    return False

#  Test the function

assert is_zero.__doc__  # Ensure the docstring is present
assert is_zero(0)       # Should return True for 0
assert not is_zero(1)   # Should return False for 1

# Check that it raises a TypeError for non-integer inputs

has_thrown = False
try:
    is_zero("nonsense")  # Passing a string to trigger an exception
except TypeError:
    has_thrown = True
assert has_thrown       # Ensure the exception was thrown

# User input testing
def test_user_input():
    try:
        user_input = input("Enter an integer to check if it is zero: ")
        user_input = int(user_input)  # Convert input to integer
        result = is_zero(user_input)
        if result:
            print("The input is zero.")
        else:
            print("The input is a non-zero integer.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
    except TypeError as e:
        print(f"Error: {e}")

# Run the user input test
test_user_input()

print("All tests passed!")
