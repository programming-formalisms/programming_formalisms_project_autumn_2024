class Parameters:
    def __init__(self, n_bacteria, n_timesteps, gradient_type, bacteria_initialization):
        self.n_bacteria = n_bacteria
        self.n_timesteps = n_timesteps
        self.gradient_type = gradient_type
        self.bacteria_initialization = bacteria_initialization
    def __repr__(self):
        return "Parameters"
    def __str__(self):
        return "(" + str(self.n_bacteria) +", " + str(self.n_timesteps) +", " + str( self.gradient_type) + ", " + str( self.bacteria_initialization)+ ")"

def set_parameters(n_bacteria, n_timesteps, gradient_type, bacteria_initialization ):
    a = Parameters(n_bacteria, n_timesteps, gradient_type, bacteria_initialization)
    return a

param = set_parameters(42,1000, "uniform", "uniform")
print(param)
print(type(param))