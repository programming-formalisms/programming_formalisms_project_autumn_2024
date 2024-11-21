class Range:
    def __init__(self, lowest, highest): #lowest and highest are coming from outside
        if lowest>highest:
            raise ValueError('Lower bound is higher than upper bound')
        self._low = lowest  # _low and _high are only for in-class use
        self._high = highest
    def get_lowest(self):
        return self._low
    def get_highest(self):
        return self._high    

x = Range(3, 10)
assert x.get_lowest() == 3
assert x.get_highest() == 10
Range(100, 10) # Must raise an exception