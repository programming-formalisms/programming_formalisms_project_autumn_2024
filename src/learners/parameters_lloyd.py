class Parameters:
    """Test documentation.

        Args:
            input_n_bacteria (_type_): _description_
            input_n_timesteps (_type_): _description_
            input_gradient_type (_type_): _description_
            input_bacteria_initialization (_type_): _description_

        Raises:
            TypeError: _description_
            TypeError: _description_
            ValueError: _description_
            ValueError: _description_
        """
    def __init__(self, input_n_bacteria, input_n_timesteps, input_gradient_type, input_bacteria_initialization):
        
        valid_gradient_type = ['uniform']
        
        if isinstance(input_n_bacteria, int) and input_n_bacteria > 0:
            self.n_bacteria = input_n_bacteria
        else:
            raise TypeError("input_n_bacteria must be positive integer")    
        
        if isinstance(input_n_timesteps, int) and input_n_timesteps > 0:
            self.n_timesteps = input_n_timesteps
        else:
            raise TypeError("input_n_timesteps must be positive integer")   
        
        if input_gradient_type in valid_gradient_type:
            self.gradient_type = input_gradient_type
        else: 
            raise ValueError(f"Gradient type must be of {valid_gradient_type}")
        
        if input_bacteria_initialization in valid_gradient_type:
            self.bacteria_initialization = input_bacteria_initialization
        else:
            raise ValueError(f"Gradient type must be of {valid_gradient_type}")
    
    def __repr__(self):
        return "Parameters"
    
    def __str__(self):
        return f"[{self.n_bacteria}, {self.n_timesteps}, {self.gradient_type}, {self.bacteria_initialization}]"
