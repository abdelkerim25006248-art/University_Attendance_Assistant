# University Attendance Assistant

# Function 1: Calculate attendance percentage
def calculate_percentage(attended, total):
    if total <= 0:
        return 0

    percentage = (attended / total) * 100
    return percentage


# Function 2: Check attendance eligibility
def check_eligibility(percentage):
    if percentage >= 75:
        return "Eligible for Examination"
    else:
        return "Not Eligible for Examination"


# Function 3: Calculate classes needed to reach 75%
def classes_needed(attended, total):
    if total <= 0:
        return "Invalid total classes"

    if attended > total or attended < 0:
        return "Invalid attendance details"

    required = 0.75 * total - attended

    if required <= 0:
        return 0

    # Additional classes must be whole numbers
    return int(required / 0.25) + (1 if required % 0.25 else 0)
