"""The Programming Formalisms Learners Project.

Project used in the UPPMAX Programming Formalisms course.
"""

import cProfile
import sys

from bacsim.simulation import (
  run_experiment,
)

if __name__ == "__main__":
    run_experiment("parameters.csv", "results.csv")
