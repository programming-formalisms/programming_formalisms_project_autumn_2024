assert is_gradient.__doc__
assert is_gradient("nonsense") == False
assert is_gradient(create_test_gradient()) == True