from attendance_pkg import (
    calculate_percentage,
    check_eligibility,
    classes_needed
)

print("==========================================")
print("       UNIVERSITY ATTENDANCE ASSISTANT")
print("==========================================")

try:
    name = input("Enter student name: ")
    total = int(input("Enter total classes conducted: "))
    attended = int(input("Enter classes attended: "))

    if total <= 0:
        print("Invalid input! Total classes must be greater than zero.")

    elif attended < 0 or attended > total:
        print("Invalid input! Check the number of classes attended.")

    else:
        percentage = calculate_percentage(attended, total)
        eligibility = check_eligibility(percentage)
        needed = classes_needed(attended, total)

        print("\n--------- ATTENDANCE REPORT ---------")
        print("Student Name:", name)
        print("Total Classes:", total)
        print("Classes Attended:", attended)
        print("Attendance Percentage:", round(percentage, 2), "%")
        print("Examination Status:", eligibility)

        if needed == 0:
            print("Additional Classes Needed: 0")
        else:
            print("Additional Classes Needed to Reach 75%:", needed)

except ValueError:
    print("Invalid input! Please enter numbers for class details.")

print("==========================================")

