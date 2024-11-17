"""The Programming Formalisms Learners Project.

Project used in the UPPMAX Programming Formalisms course.
"""

import cProfile
import sys

"""Needs to have the bacsim Python package installed.

Tip: run './scripts/install_this_package.sh'
"""
from bacsim.simulation import (
  run_experiment,
)

if __name__ == "__main__":
    run_experiment("parameters.csv", "results.csv")
