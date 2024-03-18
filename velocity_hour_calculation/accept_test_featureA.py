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
        
        # Scenario 3: Calculate Velocity for Single Sprint
        prev_sprints_pt = [10]
        self.assertEqual(calculate_velocity(prev_sprints_pt), 10)
        print("Acceptance test (Scenario 3) passed: Velocity calculated for single sprint.")

        # Scenario 4: Calculate Velocity with Negative Story Points
        prev_sprints_pt = [-10, 20, -30]
        expected_velocity = sum(prev_sprints_pt) / len(prev_sprints_pt)
        self.assertEqual(calculate_velocity(prev_sprints_pt), expected_velocity)
        print("Acceptance test (Scenario 4) passed: Velocity calculated with negative story points.")

        # Scenario 5: Calculate Velocity with Large Values
        prev_sprints_pt = [1000, 1005, 1100, 1200, 1300]
        expected_velocity = sum(prev_sprints_pt) / len(prev_sprints_pt)
        self.assertEqual(calculate_velocity(prev_sprints_pt), expected_velocity)
        print("Acceptance test (Scenario 5) passed: Velocity calculated with large values.")

if __name__ == '__main__':
    unittest.main()
