"""The Programming Formalisms Learners Project.

Project used in the UPPMAX Programming Formalisms course.

You need to have the bacsim Python package installed.

Tip: run './scripts/install_this_package.sh'
"""

from bacsim.experiment import (
    run_experiment,
)

if __name__ == "__main__":
    run_experiment("parameters.csv", "results.csv")

# test