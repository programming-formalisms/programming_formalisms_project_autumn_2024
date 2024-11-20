
import random 
import unittest

def start_coordinates(num_particles, x_range, y_range):
                      
    "Start with the 2D coordinates "

#test 
num_particles = 10            # Number of particles
x_range = (0, 100)            # X-coordinate range
y_range = (0, 100)            # Y-coordinate range

coordinates = []
for _ in range(num_particles):
        x = random.uniform(*x_range)
        y = random.uniform(*y_range)
        coordinates.append((x, y))
        
#print (coordinates)

assert start_coordinates.__doc__

assert start_coordinates