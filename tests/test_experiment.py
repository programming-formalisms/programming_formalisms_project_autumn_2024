"""Tests all code in src.bacsim.experiment."""
import unittest

from src.bacsim.experiment import run_experiment

class TestExperiment(unittest.TestCase):

    """Class to test the code in src.bacsim.experiment."""

    def test_run_experiment_exists(self):
        """The function 'run_experiment' exists."""
        run_experiment("parameters.csv", "results.csv")


