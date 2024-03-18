import unittest
from velocity_calculation import calculate_effort_hour_capacity_per_person, calculate_effort_hour_capacity_for_team

class TestFeatureBAcceptance(unittest.TestCase):
    """
    Acceptance test class for Feature B (Calculate Effort Hour Capacity per Person and for Team).
    """

    def test_calculate_effort_hour_capacity_per_person(self):
        """
        Test case to verify the calculation of effort hour capacity per person.
        """
        # Scenario: Calculate Effort Hour Capacity per Person
        num_sprint_days = 7
        team_mem_details = [
            {'hours_per_day': 6, 'time_off': [2, 0, 0]},
            {'hours_per_day': 5, 'time_off': [1, 0, 0]}
        ]
        expected_capacity_per_person = sum([6*(7-2), 5*(7-1)])  # Calculate expected capacity
        self.assertEqual(calculate_effort_hour_capacity_per_person(num_sprint_days, team_mem_details), expected_capacity_per_person)
        print("Acceptance test (Scenario) passed: Effort hour capacity per person calculated correctly.")

    def test_calculate_effort_hour_capacity_for_team(self):
        """
        Test case to verify the calculation of effort hour capacity for team.
        """
        # Scenario: Calculate Effort Hour Capacity for Team
        num_sprint_days = 7
        team_mem_details = [
            {'hours_per_day': 6, 'time_off': [2, 0, 0]},
            {'hours_per_day': 5, 'time_off': [1, 0, 0]}
        ]
        expected_capacity_for_team = sum([6*(7-2), 5*(7-1)]) * len(team_mem_details)  # Calculate expected capacity
        self.assertEqual(calculate_effort_hour_capacity_for_team(num_sprint_days, team_mem_details), expected_capacity_for_team)
        print("Acceptance test (Scenario) passed: Effort hour capacity for team calculated correctly.")

if __name__ == '__main__':
    unittest.main()
