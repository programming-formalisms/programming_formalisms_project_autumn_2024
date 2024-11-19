| Requirement ID | Requirement Description | Acceptance Criteria | Test Cases | Risk type | Risk | Risk Probability | Risk severity | Risk value
|----------------|-------------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|------------|
|R1| Simulate Bacteria and Bacteria movement | 
|R1.1              | 2D space & time         |Must have a plane with coordinates and measure of time| Be able to able to get coordinates for a point|
|R1.2              | Bacteria initialization |Bacteria must occupy space| Output bacteria position |
|R1.3              | Nutrient gradient       |Nutrient value that depends on position | Output nutrient gradient |
|R4              | Bacteria run  |Bacteria moves in single direction with constant speed. | Check the position output.|
|R5              | Bacteria tumble         |Bacteria moves in random direction. Randomly changes direction. | Check the position output and verify that it's random.|
|R6              | Bacteria must sense nutrients | Bacteria continue running along nutrient gradient.|Compare different layouts of nutrients
|R7              | End condition | Programm stops in organized manner and generates output. | Verify the output. Check that everything is cleaned up.
|R8              | Optional: Visualization | Generate a movie of the simulation. | Verify that the movie matches the simulation.
|R9              | Units                   | Allow the user to pick units | Check that units are correctly converted. 
|R10             | Concentration constraints | Warn the user of too high concentration values. | Check that warnings are raised.


| R1             | Visual Display | The program should display a field of bacterias and nutrients | Verify that the display works               |
| R2             | Particle Initialization | Find current x- and y-position and velocity of bacteria       | Confirm position and velocity for bacterias |
| R3             | Generate random direction | Pick a random direction for the 'tumble' feature              | Confrim that random direction is chosen     |
| R4             | Specify position of nutrients | Gives a map for the nutrient position in x- and y-coordinates | Verify nutrient map                         |
| R5             | Run length | Gives run-length depending on nutrient intake | Confirm accurate run-length                 |

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

| R1                  | Bacterial Initialization                  | Bacteria must be initialized with random positions, orientations, and parameters such as speed or sensing radius. | - Confirm that each bacterium is assigned unique initial positions and orientations.                             |
| R2                  | Environment Initialization                  | The simulation must initialize a 2D space with user-defined dimensions and optional gradients or features.    | - Verify the 2D space initializes correctly with all defined properties (e.g., size, chemical gradient, obstacles). |
| R3                  | Random Movement                           | Bacteria must perform random motion by default (e.g., run-and-tumble dynamics).                              | - Verify that bacteria move randomly within the field.                                                           |
| R4                  | Chemotaxis Simulation                     | Bacteria should sense and move toward higher concentrations of a chemical gradient.                          | - Implement gradient sensing. <br /> - Confirm bacteria move toward higher concentrations of the chemical.              |
| R5                  | Interaction Between Bacteria              | Bacteria must interact through collisions or quorum sensing mechanisms if specified in settings.              | - Verify that bacteria respond to each other's presence (e.g., avoid overlapping or aggregate in groups).         |
| R6                  | Boundary Conditions                       | Define boundary behavior for bacteria, such as reflecting, wrapping, or stopping at edges.                   | - Confirm bacteria behave correctly at boundaries based on the specified condition.                               |
| R7                  | Simulation Step                           | The simulation must progress in discrete steps, updating bacterial positions and orientations.                | - Verify that bacterial positions and orientations update correctly with each simulation step.                    |
| R8                 | Pause and Resume Simulation               | Allow the simulation to be paused and resumed without restarting.                                            | - Verify that pausing stops updates and resuming continues from the paused state.                                 |
| R9                 | Stop Simulation                           | Enable stopping the simulation via user interaction.                                                        | - Test that the simulation terminates cleanly when stopped.                                                      |
| R10                 | Restart Simulation                        | Allow restarting the simulation without closing the interface.                                               | - Confirm that restarting initializes the field and bacteria correctly while keeping the interface open.           |
| R11                  | Visual Display                            | The program must display a 2D field with bacteria and optional visual cues for chemical gradients or boundaries. | - Verify that the program opens a graphical window showing the bacteria's positions and relevant gradients.      |
| R12                 | Real-Time User Interaction                  | Allow users to interact with the simulation by placing bacteria, obstacles, or gradients during runtime.       | - Confirm that user interactions immediately reflect in the simulation without crashing.                             |
| R13                 | Path Visualization                          | Trace and display the paths taken by bacteria over time.                                                     | - Verify that paths are visualized correctly without overwhelming the display.                                       |
| R14                | Data Logging                              | Log data on bacterial positions, orientations, and interactions for analysis.                                | - Verify that logs are created and updated correctly with relevant simulation data.                               |
| R15                 | Statistical Analysis Tools                  | Provide built-in tools for analyzing simulation data, e.g., average speed, cluster size.                      | - Verify that summary statistics and visualizations (e.g., histograms) are accurate and match logged data.            |
| R16                 | Test-Driven Development                   | Develop the project using TDD principles.                                                                   | - Write tests before implementing each feature or functionality. <br /> - Ensure tests pass post-implementation.         |
