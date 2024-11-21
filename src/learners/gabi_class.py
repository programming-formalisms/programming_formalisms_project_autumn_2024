     
#### Gotta get 3 diff classes as discussed: velocity particle and position

class Position:
    def __init__(bacterium, any_x, any_y):
        bacterium.x = any_x
        bacterium.y = any_y
    def __repr__(bacterium):
            return "Position"
    def __str__(bacterium):
            return "(" + str(bacterium.x) + ", " + str(bacterium.y) + ")"

class Velocity:
    def __init__(bacterium, any_x, any_y):
      bacterium.x = any_x
      bacterium.y = any_y
    def __repr__(bacterium):
        return "Velocity"
    def __str__(bacterium):
        return "(" + str(bacterium.x) + ", " + str(bacterium.y) + ")"

class Particle:
    def __init__(bacterium, any_position, any_velocity):
      bacterium.position = any_position
      bacterium.velocity = any_velocity
    def __repr__(bacterium):
        return "Position"
    def __str__(bacterium):
        return (
            "Position: " + str(bacterium.position)  + ", " 
            + "velocity" + str(bacterium.velocity)
        )



