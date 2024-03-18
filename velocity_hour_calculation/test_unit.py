import unittest
from velocity_calculation import calculate_velocity, calculate_effort_hour_capacity_per_person, calculate_effort_hour_capacity_for_team

class TestVelocityCalculation(unittest.TestCase):

    def test_calculate_velocity_empty_list(self):
        prev_sprints_pt = []
        self.assertEqual(calculate_velocity(prev_sprints_pt), 0)

    def test_calculate_velocity_non_empty_list(self):
        prev_sprints_pt = [30, 85, 10, 20, 40]
        expected_velocity = sum(prev_sprints_pt) / len(prev_sprints_pt)
        self.assertEqual(calculate_velocity(prev_sprints_pt), expected_velocity)

    def test_calculate_velocity_single_item_list(self):
        prev_sprints_pt = [10]
        self.assertEqual(calculate_velocity(prev_sprints_pt), 10)

    def test_calculate_velocity_negative_numbers(self):
        prev_sprints_pt = [-10, -20, -30]
        self.assertEqual(calculate_velocity(prev_sprints_pt), -20)

class TestEffortCapacity(unittest.TestCase):

    def test_calculate_effort_hour_capacity_per_person(self):
        # Normal case
        num_sprint_days = 7
        team_mem_details = [
            {'hours_per_day': 6, 'time_off': [2, 0, 0]},
            {'hours_per_day': 5, 'time_off': [1, 0, 0]}
        ]
        expected_capacity_per_person = sum([6*(7-2), 5*(7-1)])  # Calculate expected capacity
        self.assertEqual(calculate_effort_hour_capacity_per_person(num_sprint_days, team_mem_details), expected_capacity_per_person)

        # Edge case: Zero hours per day
        team_mem_details_zero_hours = [{'hours_per_day': 0, 'time_off': [2, 0, 0]}]
        self.assertEqual(calculate_effort_hour_capacity_per_person(num_sprint_days, team_mem_details_zero_hours), 0)

        # Edge case: Negative hours per day
        team_mem_details_negative_hours = [{'hours_per_day': -5, 'time_off': [2, 0, 0]}]
        # Check if ValueError is raised when hours_per_day is negative
        with self.assertRaises(ValueError):
            calculate_effort_hour_capacity_per_person(num_sprint_days, team_mem_details_negative_hours)

        # Edge case: Empty time off list
        team_mem_details_empty_time_off = [{'hours_per_day': 6, 'time_off': []}]
        self.assertEqual(calculate_effort_hour_capacity_per_person(num_sprint_days, team_mem_details_empty_time_off), 6 * num_sprint_days)

        # Edge case: Negative time off values
        team_mem_details_negative_time_off = [{'hours_per_day': 6, 'time_off': [-2, 0, 0]}]
        # Check if ValueError is raised when time_off has negative values
        with self.assertRaises(ValueError):
            calculate_effort_hour_capacity_per_person(num_sprint_days, team_mem_details_negative_time_off)

        # Edge case: Large values
        large_num_sprint_days = 1000
        large_team_mem_details = [{'hours_per_day': 10**6, 'time_off': [0, 0, 0]}]
        expected_capacity_large_values = 10**6 * (1000 - sum([0, 0, 0]))
        self.assertEqual(calculate_effort_hour_capacity_per_person(large_num_sprint_days, large_team_mem_details), expected_capacity_large_values)

    def test_calculate_effort_hour_capacity_for_team(self):
        # Normal case
        num_sprint_days = 7
        team_mem_details = [
            {'hours_per_day': 6, 'time_off': [2, 0, 0]},
            {'hours_per_day': 5, 'time_off': [1, 0, 0]}
        ]
        expected_capacity_for_team = sum([6*(7-2), 5*(7-1)]) * len(team_mem_details)  # Calculate expected capacity
        self.assertEqual(calculate_effort_hour_capacity_for_team(num_sprint_days, team_mem_details), expected_capacity_for_team)

        # Edge case: Empty team
        empty_team_mem_details = []
        self.assertEqual(calculate_effort_hour_capacity_for_team(num_sprint_days, empty_team_mem_details), 0)

        # Edge case: Team with one member
        team_with_one_member = [{'hours_per_day': 6, 'time_off': [2, 0, 0]}]
        expected_capacity_one_member = 6 * (7 - sum([2, 0, 0]))
        self.assertEqual(calculate_effort_hour_capacity_for_team(num_sprint_days, team_with_one_member), expected_capacity_one_member)

        # Edge case: Large values
        large_team_mem_details = [{'hours_per_day': 10**6, 'time_off': [0, 0, 0]}]
        expected_capacity_large_values = (10**6 * (7 - sum([0, 0, 0]))) * len(large_team_mem_details)
        self.assertEqual(calculate_effort_hour_capacity_for_team(num_sprint_days, large_team_mem_details), expected_capacity_large_values)

if __name__ == '__main__':
    unittest.main()
