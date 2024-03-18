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
        if member_detail['hours_per_day'] < 0:
            raise ValueError("Hours per day cannot be negative")
        if any(time_off < 0 for time_off in member_detail['time_off']):
            raise ValueError("Time off cannot be negative")
        total_hours_available_per_person += member_detail['hours_per_day'] * (num_sprint_days - sum(member_detail['time_off']))
    return total_hours_available_per_person

# effort_capacity.py
def calculate_effort_hour_capacity_for_team(num_sprint_days, team_member_details):
    total_hours_available_per_team = 0
    for member_detail in team_member_details:
        total_hours_available_per_team += member_detail['hours_per_day'] * (num_sprint_days - sum(member_detail['time_off']))
    return total_hours_available_per_team * len(team_member_details)

def get_input():
    prev_sprints_pt = input("Enter sprint points (comma-separated): ").strip().split(',')
    prev_sprints_pt = [int(pt) for pt in prev_sprints_pt]
    
    num_sprint_days = int(input("Enter number of sprint days: "))
    
    team_mem_details = []
    num_team_members = int(input("Enter number of team members: "))
    for i in range(num_team_members):
        hours_per_day = int(input(f"Enter hours per day for team member {i+1}: "))
        time_off = input(f"Enter time off for team member {i+1} (comma-separated): ").strip().split(',')
        time_off = [int(off) for off in time_off]
        team_mem_details.append({'hours_per_day': hours_per_day, 'time_off': time_off})
    
    return prev_sprints_pt, num_sprint_days, team_mem_details

def main():
    prev_sprints_pt, num_sprint_days, team_mem_details = get_input()

    print(f'Velocity calculation: {calculate_velocity(prev_sprints_pt)}')
    print(f'Effort hour capacity per person : {calculate_effort_hour_capacity_per_person(num_sprint_days, team_mem_details)}')
    print(f'Effort hour capacity per person : {calculate_effort_hour_capacity_for_team(num_sprint_days, team_mem_details)}')

if __name__ == "__main__":
    main()
