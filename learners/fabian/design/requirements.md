| Requirement ID | Requirement Description | Acceptance Criteria | Test Cases |
|----------------|-------------------------|---------------------|------------|
|R1              | 2D space & time         |Must have a plane with coordinates and measure of time| Be able to able to get coordinates for a point|
|R2              | Bacteria initialization |Bacteria must occupy space| Output bacteria position |
|R3              | Nutrient gradient       |Nutrient value that depends on position | Output nutrient gradient |
|R4              | Bacteria run  |Bacteria moves in single direction with constant speed. | Check the position output.|
|R5              | Bacteria tumble         |Bacteria moves in random direction. Randomly changes direction. | Check the position output and verify that it's random.|
|R6              | Bacteria must sense nutrients | Bacteria continue running along nutrient gradient.|Compare different layouts of nutrients
|R7              | End condition | Programm stops in organized manner and generates output. | Verify the output. Check that everything is cleaned up.
|R8              | Optional: Visualization | Generate a movie of the simulation. | Verify that the movie matches the simulation.
|R9              | Units                   | Allow the user to pick units | Check that units are correctly converted. 
|R10             | Concentration constraints | Warn the user of too high concentration values. | Check that warnings are raised.
