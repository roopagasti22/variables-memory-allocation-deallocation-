required_skills = ["python", "SQL", "Git", "HTML"]


def check_skill(skill_name):
    if skill_name in required_skills:
        return "Skill available"
    return "Skill not available"


skill_name = input("Enter a skill name: ")
print(check_skill(skill_name))