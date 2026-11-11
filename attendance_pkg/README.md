# University Attendance Assistant

## Project Description
The University Attendance Assistant is a Python-based application that calculates student attendance percentages and checks whether students are eligible to appear for examinations based on the minimum attendance requirement of 75%.

It also calculates how many consecutive future classes a student needs to attend to reach 75% attendance.

## Features
- Accepts student name.
- Accepts total classes conducted.
- Accepts classes attended.
- Calculates attendance percentage.
- Checks examination eligibility.
- Calculates additional classes needed to reach 75%.
- Validates negative or invalid attendance details.
- Handles non-numeric input.

## Package Structure
```text
UniversityAttendanceAssistant/
├── main.py
└── attendance_pkg/
    ├── __init__.py
    └── ActualTask.py
```

## Functions Used

1. `calculate_percentage()` – Calculates the student's attendance percentage.
2. `check_eligibility()` – Checks whether the student has at least 75% attendance.
3. `classes_needed()` – Calculates the number of consecutive future classes required to reach 75%.

## Attendance Rule

Minimum attendance required: **75%**

Formula:

Attendance Percentage = (Classes Attended / Total Classes) × 100

## Technologies Used
- Python
- Visual Studio Code
- GitHub

## How to Run

Open the terminal in the project folder and execute:

```bash
python main.py
```

If Python is not available through the `python` command, use your installed Python executable.

## Test Cases

| Total Classes | Attended Classes | Expected Result |
|---:|---:|---|
| 100 | 80 | 80% – Eligible |
| 100 | 75 | 75% – Eligible |
| 100 | 36 | 36% – Not Eligible |
| 100 | 20 | 20% – Not Eligible |
| 100 | 120 | Invalid attendance |
| 0 | 0 | Invalid total classes |

## Conclusion
The University Attendance Assistant demonstrates Python packages, reusable functions, conditional statements, mathematical calculations, and input validation. It helps students understand their attendance percentage and examination eligibility.
