def student_result(marks):
	if marks >= 75:
		return "Distinction"
	if marks >= 35:
		return "Passed"
	return "Fail"


marks = float(input("Enter student marks: "))
print(student_result(marks))
