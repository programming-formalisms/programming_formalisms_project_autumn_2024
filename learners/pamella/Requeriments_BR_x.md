| Requirement ID | Requirement Description | Acceptance Criteria | Test Cases | Risk type | Risk | Risk Probability | Risk severity | Risk value
|----------------|-------------------------|---------------------|---------------------|---------------------|---------------------|---------------------|---------------------|------------|
| R1 | Simulate Bacteria and Bacteria movement | 
| R1.1 | 2D space & time         |Must have a plane with coordinates and measure of time| Be able to able to get coordinates for a point|
| R1.2 | Bacterial Initialization  | Bacteria must be initialized with random positions, orientations, and parameters such as speed or sensing radius. | - Confirm that each bacterium is assigned unique initial positions and orientations. |
|R1.3 | Nutrient gradient       |Nutrient value that depends on position | Output nutrient gradient |
|R1.4 | Bacteria run  |Bacteria moves in single direction with constant speed. | Check the position output.|
|R1.5 | Bacteria tumble         |Bacteria moves in random direction. Randomly changes direction. | Check the position output and verify that it's random.|
|R1.6 | Bacteria must sense nutrients | Bacteria continue running along nutrient gradient.|Compare different layouts of nutrients
|R1.7 | End condition | Program stops in organized manner and generates output. | Verify the output. Check that everything is cleaned up. 
| R1.7.1 | Run length | Gives run-length depending on nutrient intake | Confirm accurate run-length
| R1.8 | Environment Initialization | The simulation must initialize a 2D space with user-defined dimensions and optional gradients or features.| Verify the 2D space initializes correctly with all defined properties (e.g., size chemical gradient, obstacles).
|R1.8.1 | Specify position of nutrients | Gives a map for the nutrient position in x- and y-coordinates | Verify nutrient map
| R1.9 | Chemotaxis Simulation  | Bacteria should sense and move toward higher concentrations of a chemical gradient. | - Implement gradient sensing. <br /> - Confirm bacteria move toward higher concentrations of the chemical.              | Technical | bacteria would move randomly | P5 | S4 | 20
| R1.10                  | Interaction Between Bacteria              | Bacteria must interact through collisions or quorum sensing mechanisms if specified in settings.              | - Verify that bacteria respond to each other's presence (e.g., avoid overlapping or aggregate in groups).         | Technical | no bacteria interaction: unphysical | P5 | S4 | 20 
| R1.12 | Boundary Conditions  | Define boundary behavior for bacteria, such as reflecting, wrapping, or stopping at edges.  | - Confirm bacteria behave correctly at boundaries based on the specified condition. | Technical | bacteria would steadily be lost | P5 | S4 | 20
| R1.13 | Simulation Step                           | The simulation must progress in discrete steps, updating bacterial positions and orientations.                | - Verify that bacterial positions and orientations update correctly with each simulation step.                   | Technical | program does not run | P5 | S5 | 25
|R2 |Visualization | Generate a movie of the simulation. | Verify that the movie matches the simulation. | Business | visuals not working | P5 | P2 | 15
|R2.1|Visual Display | The program should display a field of bacterias and nutrients | Verify that the display works              
| R2.2 | Path Visualization                          | Trace and display the paths taken by bacteria over time.                                                     | - Verify that paths are visualized correctly without overwhelming the display.                                       |
|R3 | Units  | Allow the user to pick units | Check that units are correctly converted. 
|R4| Concentration constraints | Warn the user of too high Nutrient values. | Check that warnings are raised.
| R5  | Pause and Resume Simulation  | Allow the simulation to be paused and resumed without restarting. | - Verify that pausing stops updates and resuming continues from the paused state.  |
| R6 | Stop Simulation  | Enable stopping the simulation via user interaction.  | - Test that the simulation terminates cleanly when stopped.                                                      |
| R7 | Restart Simulation  | Allow restarting the simulation without closing the interface.  | - Confirm that restarting initializes the field and bacteria correctly while keeping the interface open. |
| R8 | Real-Time User Interaction  | Allow users to interact with the simulation by placing bacteria, obstacles, or gradients during runtime.       | - Confirm that user interactions immediately reflect in the simulation without crashing.|
| R9                | Data Logging                              | Log data on bacterial positions, orientations, and interactions for analysis.                                | - Verify that logs are created and updated correctly with relevant simulation data.                               |
| R10                 | Statistical Analysis Tools                  | Provide built-in tools for analyzing simulation data, e.g., average speed, cluster size.                      | - Verify that summary statistics and visualizations (e.g., histograms) are accurate and match logged data.            |
| R11                 | Test-Driven Development  | Develop the project using TDD principles.| - Write tests before implementing each feature or functionality. - Ensure tests pass post-implementation.         |