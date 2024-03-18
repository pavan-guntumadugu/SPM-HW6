import unittest
from velocity_calculation import calculate_velocity

class TestFeatureAAcceptance(unittest.TestCase):
    """
    Acceptance test class for Feature A (Calculate Velocity).
    """
    def test_calculate_velocity_scenario(self):
        """
        Test case to verify the calculation of velocity based on different scenarios.
        """
        # Scenario 1: Calculate Velocity for Completed Sprints
        prev_sprints_pt = [30, 85, 10, 25, 40]
        expected_velocity = sum(prev_sprints_pt) / len(prev_sprints_pt)
        self.assertEqual(calculate_velocity(prev_sprints_pt), expected_velocity)
        print("Acceptance test (Scenario 1) passed: Velocity calculated for completed sprints.")

        # Scenario 2: Calculate Velocity for Empty List
        prev_sprints_pt = []
        self.assertEqual(calculate_velocity(prev_sprints_pt), 0)
        print("Acceptance test (Scenario 2) passed: Velocity calculated for empty list.")

if __name__ == '__main__':
    unittest.main()
