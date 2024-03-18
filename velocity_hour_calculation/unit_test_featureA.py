import unittest
from velocity_calculation import calculate_velocity
class TestVelocityCalculation(unittest.TestCase):
    def test_calculate_velocity_empty_list(self):
        # Test case for empty list
        prev_sprints_pt = []
        self.assertEqual(calculate_velocity(prev_sprints_pt), 0)

    def test_calculate_velocity_non_empty_list(self):
        # Test case for non-empty list
        prev_sprints_pt = [30, 85, 10, 20, 40]
        expected_velocity = sum(prev_sprints_pt) / len(prev_sprints_pt)
        self.assertEqual(calculate_velocity(prev_sprints_pt), expected_velocity)

    def test_calculate_velocity_single_item_list(self):
        # Test case for single item list
        prev_sprints_pt = [10]
        self.assertEqual(calculate_velocity(prev_sprints_pt), 10)

    def test_calculate_velocity_negative_numbers(self):
        # Test case for negative numbers in the list
        prev_sprints_pt = [-10, -20, -30]
        self.assertEqual(calculate_velocity(prev_sprints_pt), -20)

if __name__ == '__main__':
    unittest.main()
