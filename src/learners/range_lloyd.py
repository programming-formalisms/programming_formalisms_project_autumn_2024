class Range:
    def __init__(self, any_lowest, any_highest):
        """
        Initializing the Range class with any_highest 
        """
        assert any_lowest <= any_highest
        assert type(any_lowest) == int
        assert type(any_highest) == int
        
        self.lowest = any_lowest
        self.highest = any_highest
        
    def get_lowest(self):
        """
        return the lowest
        """
        return self.lowest
    
    def get_highest(self):
        """
        return the highest 
        """
        return self.highest

x = Range(3, 10)
assert x.get_lowest() == 3
assert x.get_highest() == 10    
#Range(100, 10) # Must raise an exception