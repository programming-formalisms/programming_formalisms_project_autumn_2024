class Range:
    def __init__(self, lowest, highest):
        assert lowest <= highest
        assert type(lowest) == int
        assert type(highest) == int
        self.lowest = lowest
        self.highest = highest
    
    def get_lowest(self):
        return self.lowest
    def get_highest(self):
        return self.highest
    

a = Range(3,9)
print(a)
print(type(a))

assert a.get_lowest()  == 3
assert a.get_highest() == 9