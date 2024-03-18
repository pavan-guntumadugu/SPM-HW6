from velocity_calculation import calculate_velocity, calculate_effort_hour_capacity_per_person, calculate_effort_hour_capacity_for_team
def test_feature_a_acceptance():
    # Scenario: Calculate velocity based on previous sprint points
    prev_sprints_pt = [30, 85, 10, 25, 40]
    expected_velocity = 38
    calculated_velocity = calculate_velocity(prev_sprints_pt)
    assert calculated_velocity == expected_velocity, f"Expected velocity: {expected_velocity}, Actual velocity: {calculated_velocity}"

def test_feature_b_acceptance():
    # Scenario: Calculate effort hour capacity for team members and entire team
    num_sprint_days = 7
    team_mem_details = [
        {'hours_per_day': 6, 'time_off': [2, 0, 0]},
        {'hours_per_day': 5, 'time_off': [1, 0, 0]}
    ]
    expected_capacity_per_person = sum([6*(7-2), 5*(7-1)])  # Calculate expected capacity per person
    expected_capacity_for_team = expected_capacity_per_person * len(team_mem_details)  # Calculate expected capacity for team
    
    # Calculate capacity per person
    calculated_capacity_per_person = calculate_effort_hour_capacity_per_person(num_sprint_days, team_mem_details)
    assert calculated_capacity_per_person == expected_capacity_per_person, f"Expected capacity per person: {expected_capacity_per_person}, Actual capacity per person: {calculated_capacity_per_person}"

    # Calculate capacity for team
    calculated_capacity_for_team = calculate_effort_hour_capacity_for_team(num_sprint_days, team_mem_details)
    assert calculated_capacity_for_team == expected_capacity_for_team, f"Expected capacity for team: {expected_capacity_for_team}, Actual capacity for team: {calculated_capacity_for_team}"

def run_acceptance_tests():
    try:
        test_feature_a_acceptance()
        test_feature_b_acceptance()
        print("All acceptance tests passed successfully.")
    except AssertionError as e:
        print(f"Acceptance test failed: {e}")

if __name__ == "__main__":
    run_acceptance_tests()
