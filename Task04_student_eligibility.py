def check_eligibility(marks, attendance_percentage, backlog_status):
    if marks >= 60 and attendance_percentage >= 75 and not backlog_status:
        return "Eligible"
    return "Not eligible"


marks = float(input("Enter student marks: "))
attendance_percentage = float(input("Enter attendance percentage: "))
backlog_status = input("Does the student have a backlog? (yes/no): ").strip().lower() == "yes"

print(check_eligibility(marks, attendance_percentage, backlog_status))