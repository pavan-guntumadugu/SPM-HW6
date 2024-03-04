# velocity_calculation.py
def calculate_velocity(prev_sprints_pt):
    if not prev_sprints_pt:
        return 0
    total_pt = sum(prev_sprints_pt)
    return total_pt / len(prev_sprints_pt)

prev_sprints_pt = [30, 85, 10, 25, 40]
print(calculate_velocity(prev_sprints_pt))