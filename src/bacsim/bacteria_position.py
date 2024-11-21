class Bacteria_position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Bacteria_position"
    def __str__(self):
        #return "(" + str(self.x) + ", " + str(self.y) + ")"
        return f"{self.x}, {self.y}"

a = Bacteria_position(2,2)
print(a)
