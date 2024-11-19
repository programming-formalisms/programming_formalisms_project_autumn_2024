| Requirement ID | Requirement Description | Acceptance Criteria | Test Cases |
|----------------|-------------------------|---------------------|------------|
|R01|Initialise environment| Program must initialise a 2D grid in which bacteria and nutrients could occupy space | Program when started dispays a 2D grid with bacteria
|R02|Initialise bacteria with flagellum | The program must display bacteria in a 2D grid environment | Verify that bacteria are displayed on the 2D grid with identifiable properties (e.g., size, shape, or flagellum).
|R03| Simulate run movement with clock-wise and counter clock wise movements| Bacteria must be able to run in a straight line at constant speeds| Test that bacteria move in straight lines with speeds consistent across simulation steps.
|R04| Simulate tumble movements| Bacteria must be able to tumble and change directions | Verify that bacteria change directions randomly during tumbling phases.
|R05| Change between run and tumble| Bacteria must be able to dynamically change between run and tumble movements depending on the environment |Confirm bacteria transition between run and tumble states based on nutrient gradients or other programmed cues.
|R06| Nutrient driven movements| Run durations increase as long as nutrient concentrations are increasing |Measure run durations at different nutrient levels and confirm correlation with increasing concentrations.
|R06| Pause and resume simulation (optional)| Should be able to pause and resume simulation at any point | Implement a user interface which could pause/resume the simulation when needed. Test that simulation resumes at the point at which it was stopped.
|R07| Generate log files of simulation run | Record positions and directions of the bacteria, nutrient levels for all bacteria at every (second or any other time measurement) | Validate log files to ensure they capture position, direction, and nutrient data for all bacteria at each time step.
|R08| Generate result files for further analysis (optional) |Output results in a format suitable for downstream analysis (e.g., CSV or JSON) | Confirm result files include final positions, directions, and nutrient consumption for all bacteria.
|R09| Have a stopping criteria, when does simulationstop  |
|R10| Model in the fact that bacteria would eat the nutrients |