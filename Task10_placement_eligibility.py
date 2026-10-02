def check_placement_eligibility(age, marks, attendance, experience, has_backlog):
    placement_eligible = marks >= 60 and attendance >= 75 and not has_backlog

    experience_categories = {
        "0": "Fresher",
        "1-2": "Junior",
        "more than 2": "Experienced",
    }
    candidate_category = experience_categories.get(experience.strip().lower(), "Unknown")

    return placement_eligible, candidate_category


age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance percentage: "))
experience = input("Enter experience (0, 1-2, or more than 2): ")
has_backlog = input("Does the candidate have a backlog? (yes/no): ").strip().lower() == "yes"

placement_eligible, candidate_category = check_placement_eligibility(
    age, marks, attendance, experience, has_backlog
)

print("Placement eligible:", "Yes" if placement_eligible else "No")
print("Candidate category:", candidate_category)