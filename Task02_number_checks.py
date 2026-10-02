def check_number(number):
	return {
		"even": number % 2 == 0,
		"divisible_by_3": number % 3 == 0,
		"divisible_by_5": number % 5 == 0,
	}


number = int(input("Enter an integer: "))
checks = check_number(number)

print("Even:", checks["even"])
print("Odd:", not checks["even"])
print("Divisible by 3:", checks["divisible_by_3"])
print("Divisible by 5:", checks["divisible_by_5"])
