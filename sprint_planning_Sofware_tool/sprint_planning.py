# velocity_calculation.py
def calculate_velocity(prev_sprints_pt):
    if not prev_sprints_pt:
        return 0
    total_pt = sum(prev_sprints_pt)
    return total_pt / len(prev_sprints_pt)

# effort_capacity.py
def calculate_effort_hour_capacity_per_person(num_sprint_days, team_member_details):
    total_hours_available_per_person = 0
    for member_detail in team_member_details:
        total_hours_available_per_person += member_detail['hours_per_day'] * (num_sprint_days - sum(member_detail['time_off']))
    return total_hours_available_per_person

# effort_capacity.py
def calculate_effort_hour_capacity_for_team(num_sprint_days, team_member_details):
    total_hours_available_per_team = 0
    for member_detail in team_member_details:
        total_hours_available_per_team += member_detail['hours_per_day'] * (num_sprint_days - sum(member_detail['time_off']))
    return total_hours_available_per_team * len(team_member_details)


prev_sprints_pt = [30, 85, 10, 25, 40]
number_sprint_days = 7
team_mem_details = [
    {'hours_per_day': 6, 'time_off': [2, 0, 0]},  # Example details for team member 1
    {'hours_per_day': 5, 'time_off': [1, 0, 0]}   # Example details for team member 2
]

print(f'Velocity calculation: {calculate_velocity(prev_sprints_pt)}')
print(f'Effort hour capacity per person : {calculate_effort_hour_capacity_per_person(number_sprint_days, team_mem_details)}')
print(f'Effort hour capacity per person : {calculate_effort_hour_capacity_for_team(number_sprint_days, team_mem_details)}')
