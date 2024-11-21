from logging import setLogRecordFactory


def is_zero(x):
    """Determines if input is zero.
    Will return True if input is zero.
    Will return False if input is not zero.
    Will raise an exception if input type is not integer."""

    if not isinstance(x, int):
        raise TypeError("'x' must be of type int")
    if x == 0:
        return True
    elif x != 0:
        return False



assert is_zero.__doc__
assert is_zero(0) == True

# must raise an exception if the input type is not an integer
has_thrown = False
try:
    is_zero("nonsense")
except:
    has_thrown = True
assert has_thrown

#test



class Coordinate:
    def __init__(self, any_x, any_y):
      self.x = any_x
      self.y = any_y
    def __repr__(self):
        return "Coordinat"
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Parameters:
    def __init__(self, any_n_bacteria, any_n_timesteps, any_gradient_type, any_bacteria_initialization):
        self.n_bacteria = any_n_bacteria
        self.n_timesteps = any_n_timesteps
        self.gradient_type = any_gradient_type
        self.bacteria_initialization = any_bacteria_initialization
    def __repr__(self):
        return "Parameters"
    def __str__(self):
        return "(" + str(self.n) + ", " + str(self.n_time) + ", " + str(self.type) +  ", " + str(self.init) + ")"


def get_parameter():
    return Parameters(42, 1000, 'uniform', 'uniform')

a = get_parameter()
print(a)
print(type(a))




