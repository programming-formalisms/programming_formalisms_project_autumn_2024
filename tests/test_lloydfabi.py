import unittest

from src.learners.parameters_lloyd import Parameters

class TestParameters(unittest.TestCase):

    def test_parameters_construction(self):
        test_parameter = Parameters(10, 10, "uniform", "uniform")
        self.assertEqual(str(test_parameter), "[10, 10, uniform, uniform]")
        self.assertIsInstance(test_parameter, Parameters)
        self.assertIsNotNone(test_parameter.__doc__)
