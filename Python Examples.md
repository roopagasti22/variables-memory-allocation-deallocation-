# Python Examples

This guide covers all 10 `.py` files found in this folder and its subfolders. Source code is shown as it appears in the files. The examples in `function.py` are all commented out, so Python ignores them unless the comment marks are removed.

---

## 1. `Task02_number_checks.py`

### Program 1: Checking number properties

**What it does:** Takes an integer and reports whether it is even or odd, and whether it is divisible by 3 and 5.

**Code:**

```python
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
```

### Line-by-line explanation

- `def check_number(number):` defines a function named `check_number`. `number` is a parameter: a named input the function will receive.
- `return { ... }` sends a dictionary back to the caller. A dictionary stores values under keys.
- `"even": number % 2 == 0` uses `%` (remainder) to see whether division by 2 leaves no remainder. `==` tests equality. The result is `True` or `False`.
- `"divisible_by_3": number % 3 == 0` and `"divisible_by_5": number % 5 == 0` perform the same kind of test for 3 and 5.
- `number = int(input(...))` displays a prompt, reads text typed by the user, and converts it to an integer with `int()`.
- `checks = check_number(number)` calls the function and stores its returned dictionary.
- `checks["even"]`, `checks["divisible_by_3"]`, and `checks["divisible_by_5"]` look up values by dictionary key.
- `not checks["even"]` reverses a Boolean value: `True` becomes `False` and `False` becomes `True`. Here it gives the odd result.
- `print(...)` displays each label and result.

### How it works

1. Python defines `check_number`.
2. The program asks for an integer and converts the answer from text to an integer.
3. It calls `check_number`, which calculates three Boolean results and returns them in a dictionary.
4. The program prints the stored results. It does not need a separate oddness calculation because an integer that is not even is odd.

**Example**

Input:

```text
Enter an integer: 15
```

Output:

```text
Even: False
Odd: True
Divisible by 3: True
Divisible by 5: True
```

### Important concepts

- **Function:** A reusable named block of code, introduced with `def`.
- **Parameter and argument:** `number` is the parameter in the definition; the value entered and passed to the function is its argument.
- **Dictionary:** A collection of key/value pairs, such as `"even": True`.
- **Modulo (`%`):** Gives the remainder after division.
- **Boolean:** A truth value, either `True` or `False`.
- **`return`:** Sends a result back from a function.
- **`int()` and `input()`:** `input()` reads text; `int()` converts suitable text to a whole number.

---

## 2. `Task03_student_result.py`

### Program 1: Finding a student's result category

**What it does:** Reads marks and classifies the student as having distinction, passing, or failing marks.

**Code:**

```python
def student_result(marks):
	if marks >= 75:
		return "Distinction"
	if marks >= 35:
		return "Passed"
	return "Fail"


marks = float(input("Enter student marks: "))
print(student_result(marks))
```

### Line-by-line explanation

- `def student_result(marks):` defines a function that receives the marks.
- `if marks >= 75:` checks whether marks are greater than or equal to 75. If true, the indented line runs.
- `return "Distinction"` sends that category back and immediately ends this function call.
- `if marks >= 35:` runs only if the first condition was false. It checks whether the marks are at least 35.
- `return "Passed"` returns the passing category if the second condition is true.
- `return "Fail"` runs if neither earlier condition was true.
- `marks = float(input(...))` reads the user's text and converts it to a decimal number using `float()`.
- `print(student_result(marks))` calls the function with the entered marks and displays what it returns.

### How it works

1. The program asks for marks and converts them to a number.
2. It checks the highest threshold first: 75 or more gives `Distinction`.
3. If that condition is false, it checks the passing threshold: 35 or more gives `Passed`.
4. Any lower value gives `Fail`.

**Example**

Input:

```text
Enter student marks: 82.5
```

Output:

```text
Distinction
```

### Important concepts

- **`if`:** Runs its indented block only when its condition is true.
- **`>=`:** Means “greater than or equal to.”
- **`return`:** Ends the current function call and gives a result to the caller.
- **`float()`:** Converts suitable text, such as `"82.5"`, into a decimal number.

**Note about input:** The program does not check whether marks are between 0 and 100. For example, a value greater than 100 is still classified as `Distinction`, and a negative value is classified as `Fail`.

---

## 3. `Task04_student_eligibility.py`

### Program 1: Checking student eligibility

**What it does:** Marks a student eligible only if marks are at least 60, attendance is at least 75%, and the student does not have a backlog.

**Code:**

```python
def check_eligibility(marks, attendance_percentage, backlog_status):
    if marks >= 60 and attendance_percentage >= 75 and not backlog_status:
        return "Eligible"
    return "Not eligible"


marks = float(input("Enter student marks: "))
attendance_percentage = float(input("Enter attendance percentage: "))
backlog_status = input("Does the student have a backlog? (yes/no): ").strip().lower() == "yes"

print(check_eligibility(marks, attendance_percentage, backlog_status))
```

### Line-by-line explanation

- `def check_eligibility(marks, attendance_percentage, backlog_status):` defines a function with three parameters.
- `if marks >= 60 and attendance_percentage >= 75 and not backlog_status:` checks three conditions together.
- `and` means every condition must be true. `not backlog_status` is true when the backlog value is `False`, meaning no backlog.
- `return "Eligible"` gives the eligible result when all three requirements are met.
- `return "Not eligible"` is reached if any requirement is not met.
- The two `float(input(...))` lines read marks and attendance and convert them to decimal numbers.
- `input(...).strip().lower()` reads the backlog answer, removes spaces from its ends, and makes the text lowercase.
- `== "yes"` makes the backlog variable a Boolean: it is `True` only if the cleaned answer is exactly `"yes"`. Any other answer becomes `False`.
- `print(check_eligibility(...))` calls the function using the three entered values and displays its returned text.

### How it works

1. The user enters marks, attendance, and a backlog answer.
2. Marks and attendance become numbers. The backlog answer becomes `True` only for `yes` (ignoring letter case and spaces around it).
3. The function checks the two numeric thresholds and the absence of a backlog.
4. It returns and prints either `Eligible` or `Not eligible`.

**Example**

Input:

```text
Enter student marks: 80
Enter attendance percentage: 78
Does the student have a backlog? (yes/no): no
```

Output:

```text
Eligible
```

### Important concepts

- **`and`:** All joined conditions must be true.
- **`not`:** Reverses a Boolean value.
- **`strip()`:** Removes whitespace at the beginning and end of text.
- **`lower()`:** Changes letters to lowercase.
- **`==`:** Compares two values for equality.
- **Function arguments:** The entered values are passed in the same order as the function's parameters.

**Note about input:** This program does not validate that marks and attendance are within a realistic range. It also treats every backlog answer other than `yes` as “no.”

---

## 4. `Task05_login_validation.py`

### Program 1: Checking a username and password

**What it does:** Compares the entered username and password with one fixed pair of values.

**Code:**

```python
def validate_user(username, password):
    return username == "Admin" and password == "python123"


username = input("Enter username: ")
password = input("Enter password: ")

if validate_user(username, password):
    print("Valid user")
else:
    print("Invalid user")
```

### Line-by-line explanation

- `def validate_user(username, password):` defines a function that receives two text values.
- `username == "Admin"` checks for an exact match with `Admin`.
- `password == "python123"` checks for an exact match with `python123`.
- `and` requires both comparisons to be true. The `return` sends that combined `True` or `False` result back.
- The two `input(...)` lines ask the user for the username and password. `input()` returns text.
- `if validate_user(username, password):` calls the function and tests its Boolean result.
- `print("Valid user")` runs if the result is true.
- `else:` introduces the alternative block, which runs when the condition is false.
- `print("Invalid user")` displays the alternative result.

### How it works

1. The program reads the username and password as text.
2. It passes both strings to `validate_user`.
3. The function returns `True` only when both exact comparisons match.
4. The `if/else` prints the corresponding message.

**Example**

Input:

```text
Enter username: Admin
Enter password: python123
```

Output:

```text
Valid user
```

### Important concepts

- **String:** Text such as `"Admin"`.
- **`and`:** Requires both login checks to succeed.
- **`if/else`:** Chooses one of two blocks based on a condition.
- **Boolean return value:** The function returns `True` or `False`.

**Note about behavior:** Matching is case-sensitive and exact. `admin`, `Admin ` (with a trailing space), or a different password will not match. This is a simple learning example, not a secure real-world login system: its fixed password is written in the program.

---

## 5. `Task06_purchase_discount.py`

### Program 1: Calculating a purchase discount

**What it does:** Chooses a discount rate based on the purchase total, then returns both the discount and the amount payable.

**Code:**

```python
def calculate_discount(purchase_amount):
    if purchase_amount >= 5000:
        discount_rate = 0.20
    elif purchase_amount >= 3000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount_amount = purchase_amount * discount_rate
    final_payable_amount = purchase_amount - discount_amount
    return discount_amount, final_payable_amount


purchase_amount = float(input("Enter purchase amount in ₹: "))
discount, payable = calculate_discount(purchase_amount)

print(f"Discount amount: ₹{discount:.2f}")
print(f"Final payable amount: ₹{payable:.2f}")
```

### Line-by-line explanation

- `def calculate_discount(purchase_amount):` defines a function that receives the purchase total.
- `if purchase_amount >= 5000:` selects a 20% discount for totals of 5000 or more.
- `elif purchase_amount >= 3000:` is checked only if the first condition was false. It selects 10% for totals from 3000 up to (but not including) 5000.
- `else:` selects 5% when neither earlier condition matched.
- `discount_rate = 0.20`, `0.10`, or `0.05` stores the chosen rate as a decimal. For example, `0.20` means 20%.
- `discount_amount = purchase_amount * discount_rate` multiplies the total by the rate to find the discount.
- `final_payable_amount = purchase_amount - discount_amount` subtracts the discount from the original total.
- `return discount_amount, final_payable_amount` returns two values. Python packages these values as a tuple.
- `float(input(...))` reads the amount and converts it to a decimal number.
- `discount, payable = calculate_discount(purchase_amount)` calls the function and unpacks its two returned values into two variables.
- `f"..."` makes an f-string so values can be inserted using `{...}`.
- `:.2f` formats each number to two digits after the decimal point.

### How it works

1. The program asks for a purchase amount.
2. The function selects one of three discount rates.
3. It calculates the discount and subtracts it from the purchase amount.
4. The function returns both amounts; the calling code stores and prints them with two decimal places.

**Example**

Input:

```text
Enter purchase amount in ₹: 4000
```

Output:

```text
Discount amount: ₹400.00
Final payable amount: ₹3600.00
```

### Important concepts

- **`if/elif/else`:** Chooses one matching branch. The order matters: the largest threshold is tested first.
- **Comparison (`>=`):** Checks whether a number is at least the threshold.
- **Tuple return:** The function returns two values together.
- **Unpacking:** `discount, payable = ...` assigns the first returned value to `discount` and the second to `payable`.
- **F-string:** Inserts values into text.
- **Number formatting (`:.2f`):** Shows two decimal places.

**Note about input:** No check prevents a negative purchase amount. A negative input is treated by the `else` branch and receives a 5% calculation too.

---

## 6. `Task07_access_control.py`

### Program 1: Checking access conditions

**What it does:** Grants access when a person is at least 18 and has an ID, or when the person is an employee.

**Code:**

```python
def check_access(age, has_id, is_employee):
    if (age >= 18 and has_id) or is_employee:
        return "Access granted"
    return "Access denied"


age = int(input("Enter age: "))
has_id = input("Do you have an ID? (yes/no): ").strip().lower() == "yes"
is_employee = input("Are you an employee? (yes/no): ").strip().lower() == "yes"

print(check_access(age, has_id, is_employee))
```

### Line-by-line explanation

- `def check_access(age, has_id, is_employee):` defines a function with a number and two Boolean inputs.
- `(age >= 18 and has_id)` means the person is an adult and has an ID. Parentheses make this part of the rule clear.
- `or is_employee` means an employee is also allowed, even if the first parenthesized condition is false.
- `if ...:` runs the next line when the whole expression is true.
- `return "Access granted"` and `return "Access denied"` send one of the two messages back.
- `age = int(input(...))` reads an age and converts it to a whole number.
- Each yes/no input is stripped of outer spaces, changed to lowercase, and compared with `"yes"`. The result is `True` only for yes.
- `print(check_access(...))` calls the function with the three values and displays its answer.

### How it works

1. The program reads an age and two yes/no answers.
2. It converts the age to an integer and the answers to Boolean values.
3. Access is granted if both adult-and-ID checks pass, or if the employee check passes.
4. The function returns the decision and `print` displays it.

**Example**

Input:

```text
Enter age: 16
Do you have an ID? (yes/no): no
Are you an employee? (yes/no): yes
```

Output:

```text
Access granted
```

### Important concepts

- **`and`:** Both parts must be true.
- **`or`:** At least one side must be true.
- **Parentheses:** Group the adult-and-ID rule together.
- **Short-circuit evaluation:** With `or`, Python does not need to test the right side if the left side is already true. Similarly, with `and`, it can stop once a part is false.
- **Boolean inputs:** The comparisons against `"yes"` produce `True` or `False`.

---

## 7. `Task08_skill_check.py`

### Program 1: Checking whether a skill is in a list

**What it does:** Checks whether the entered skill matches one of four required skills.

**Code:**

```python
required_skills = ["python", "SQL", "Git", "HTML"]


def check_skill(skill_name):
    if skill_name in required_skills:
        return "Skill available"
    return "Skill not available"


skill_name = input("Enter a skill name: ")
print(check_skill(skill_name))
```

### Line-by-line explanation

- `required_skills = [...]` creates a list containing four strings.
- `def check_skill(skill_name):` defines a function that receives the skill name to look for.
- `if skill_name in required_skills:` uses `in` to test whether the value is present in the list.
- `return "Skill available"` returns this message when the value is found.
- `return "Skill not available"` runs when the `if` condition is false.
- `skill_name = input(...)` reads the user's answer as text.
- `print(check_skill(skill_name))` passes the answer to the function and displays the returned message.

### How it works

1. Python creates the `required_skills` list and defines the function.
2. The program asks the user to type a skill.
3. The function checks whether that exact string occurs in the list.
4. The program prints the result.

**Example**

Input:

```text
Enter a skill name: SQL
```

Output:

```text
Skill available
```

### Important concepts

- **List:** An ordered collection written with square brackets, such as `["python", "SQL"]`.
- **`in`:** Tests membership: whether a value appears in a collection.
- **`return`:** Sends the selected message back to the caller.

**Note about matching:** Text comparison is case-sensitive, and the program does not trim spaces. `python` matches but `Python` does not; `SQL ` with a trailing space does not match `SQL`.

---

## 8. `Task09_calculator_function.py`

### Program 1: A basic calculator function

**What it does:** Performs addition, subtraction, multiplication, division, floor division, or remainder, and displays an error for an unsupported operator or a zero divisor.

**Code:**

```python
def calculate(a, operator, b):
    valid_operators = ("+", "-", "*", "/", "//", "%")
    if operator not in valid_operators:
        raise ValueError("Invalid operator")

    if operator in ("/", "//", "%") and b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b
    if operator == "//":
        return a // b
    return a % b


first_number = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /, //, %): ")
second_number = float(input("Enter the second number: "))

try:
    print("Result:", calculate(first_number, operator, second_number))
except (ValueError, ZeroDivisionError) as error:
    print("Error:", error)
```

### Line-by-line explanation

- `def calculate(a, operator, b):` defines a function. `a` and `b` are the numbers; `operator` is the requested operation.
- `valid_operators = (...)` creates a tuple of the operators this program accepts. A tuple is an ordered collection, often used for fixed items.
- `if operator not in valid_operators:` checks whether the operator is absent from that tuple.
- `raise ValueError("Invalid operator")` deliberately reports an invalid operator by raising an exception (an error condition).
- `if operator in ("/", "//", "%") and b == 0:` checks whether the operation needs division and the second number is zero.
- `raise ZeroDivisionError(...)` reports that division by zero is not allowed.
- Each `if operator == ...:` selects an operation. `+`, `-`, and `*` mean addition, subtraction, and multiplication.
- `/` performs ordinary division; `//` performs floor division (for example, `7.0 // 2.0` is `3.0`); `%` returns the remainder.
- Each `return` immediately ends the function call with that operation's result.
- The final `return a % b` is reached when the earlier checks have passed and the operator is `%`.
- The two `float(input(...))` lines read the numbers and convert them to decimal numbers.
- `operator = input(...)` reads the operator as text.
- `try:` begins a block where the program expects a possible error.
- `except (ValueError, ZeroDivisionError) as error:` catches either of those two error types and stores the error object in `error`.
- `print("Error:", error)` displays the error message rather than allowing those caught errors to stop the program.

### How it works

1. The program reads two numbers and an operator.
2. Inside `try`, it calls `calculate`.
3. The function first rejects an unknown operator, then rejects a zero divisor for division-type operations.
4. It returns the selected arithmetic result.
5. If one of the two listed errors occurs during the function call, the `except` block prints an error message.

**Example**

Input:

```text
Enter the first number: 10
Enter an operator (+, -, *, /, //, %): *
Enter the second number: 3
```

Output:

```text
Result: 30.0
```

For example, entering `/` and `0` for the operator and second number prints:

```text
Error: Cannot divide by zero
```

### Important concepts

- **Tuple:** Fixed ordered values in parentheses.
- **`in` / `not in`:** Check whether an item is present or absent in a collection.
- **`raise`:** Creates an exception to report an error.
- **`try/except`:** Runs code that might produce an error and handles the specified error types.
- **`//`:** Floor division; with positive numbers, it gives the whole-number portion of the quotient, while the result here is still a float because the inputs are floats.
- **`%`:** Remainder after division.

**Important limitation:** Converting the first and second inputs with `float()` happens before the `try` block. If the user types non-numeric text for either number, the resulting `ValueError` is not caught by this program's `except` block. The error handling covers errors raised during the call to `calculate`, not errors from those earlier conversions.

---

## 9. `Task10_placement_eligibility.py`

### Program 1: Checking placement eligibility and candidate category

**What it does:** Checks placement eligibility using marks, attendance, and backlog status, and maps an experience label to a category.

**Code:**

```python
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
```

### Line-by-line explanation

- `def check_placement_eligibility(age, marks, attendance, experience, has_backlog):` defines a function with five parameters.
- `placement_eligible = marks >= 60 and attendance >= 75 and not has_backlog` stores `True` only if marks are at least 60, attendance is at least 75, and there is no backlog.
- `experience_categories = {...}` creates a dictionary mapping each accepted experience label to a category.
- `experience_categories.get(key, "Unknown")` looks up the key. If it is not present, `.get()` supplies `"Unknown"` instead of raising a missing-key error.
- `experience.strip().lower()` removes spaces at the ends and changes the label to lowercase before lookup.
- `return placement_eligible, candidate_category` returns two values together as a tuple.
- `age = int(input(...))` reads and converts age to an integer.
- The marks and attendance lines read and convert those values to decimal numbers.
- `experience = input(...)` reads the experience label as text.
- The backlog line strips outer spaces, changes the answer to lowercase, and sets `has_backlog` to `True` only when the answer is `"yes"`.
- The function call passes the five values in parameter order.
- `placement_eligible, candidate_category = ...` unpacks the returned pair into two variables.
- `"Yes" if placement_eligible else "No"` is a conditional expression: it chooses `"Yes"` when the condition is true and `"No"` otherwise.
- The two `print(...)` calls display the eligibility and category.

### How it works

1. The program reads the five requested values.
2. It converts age, marks, and attendance to numbers, and converts the backlog answer to a Boolean.
3. The function calculates eligibility and looks up the experience category separately.
4. It returns both results, which are unpacked and printed.

**Example**

Input:

```text
Enter age: 22
Enter marks: 75
Enter attendance percentage: 80
Enter experience (0, 1-2, or more than 2): 1-2
Does the candidate have a backlog? (yes/no): no
```

Output:

```text
Placement eligible: Yes
Candidate category: Junior
```

### Important concepts

- **Dictionary lookup:** Uses a label as a key to find a category.
- **`.get()`:** Looks up a key and supplies a fallback value when it is missing.
- **Tuple return and unpacking:** Two results are returned and assigned to two variables.
- **Conditional expression:** `value_if_true if condition else value_if_false` chooses one of two values.
- **`and` and `not`:** Combine requirements and test that the backlog flag is false.

**Important limitation:** `age` is accepted by the function and entered by the user, but it is never used in the eligibility calculation or category lookup. Therefore changing age does not change either answer. The category lookup also accepts only the labels `"0"`, `"1-2"`, and `"more than 2"` (ignoring letter case and outer spaces); other wording gives `Unknown`.

---

## 10. `function.py`

### Program 1: Function teaching examples

**What it does:** This file is a collection of small teaching examples about functions, parameters, return values, variable scope, lambdas, recursion, documentation strings, annotations, and breaking a large task into smaller functions. **Every line in this file is commented out**, so running this file as it is produces no output and does not run any of the examples.

**Code:**

```python
# print ("Roopa")
# print ("Sakshi")
# print ("kavya")

# def add(a,b):   
#     return a+b
# add (2,3)

# def welcome (name):
#     print("welcome", name)
# welcome("Roopa")
# welcome("nidi")
# welcome("Shree")

# def greet():
#     print ("hello")
# greet()

# def welcome():
#      print("welcome to nighan2 labs")
# welcome()

# def welcome(name):
#     print("welcome",name)
# welcome("Roopa")

# def add(a,b):
#     print (a+b)
# add(10,20)



# def add(a,b):
#     print(a+b) 
#     return a+b
# result =add(10,20)
# print(result)

# def test():
#    return 10
# print("Hello")

# def calculate(a,b):
#     return a+b, a-b, a*b

# X,Y,Z = calculate (10,5)
# print(X)
# print(Y)
# print(Z)

# def greet (name ="Roopa"):
#      print("hello",name)
# greet ()
# greet("arati")

# def student (name, age):
#      print(name, age)
# student("Roopa",20) 

# students(age =21,name ="Roopa")
# print(name, age)

# def student(name , age ,course):
#      print(name, age, course )
# student("Roopa",age=21,course="BCA")

# def add(*numbers):
#     total = 0 
#     for number in numbers:
#         total += number 
#     return total

# print(add(10,20))
# print(add(10,20,30))
# print(add(1,2,3,4,5))

# def student(**details): 
#     print(details)

# student(name="Roopa", age=21, course="BCA")

# def example(a, b=10,*args, **kwargs ):
#     pass def test():

# def test():
#     X=10
#     print(X)
# test()

# X = 100
# def test():
#     print(X)
# test()


# count = 0
# def increment():
#     global count
#     count += 1
# increment()
# print(count)



# def test():
#     X=10
# test()
# print(X)
 
# def add(a, b):
#     return a+b
# def display():
#     result = add(10,20)
#     print(result)

# display()

# def multiply (a,b):
#     return a*b
# result = multiply(5,4)
# print(result)

# def square(x):
#      return x*x
# def process(function, value):
#      return function(value)
# print(process(square,5))

# square = lambda x: x*x
# print(square(5))

# numbers =(1,2,3,4)
# result = list(map(lambda x: x*2,numbers))
# print(result)

# def countdown (n):
#      if n == 0:
#         return 
#      print(n)
#      countdown (n-1)
# countdown (5)

# def add(a,b):
#     """return the sum of two numbers """
#     return a+b


# print(add.__doc__)  

# def add(a: int, b: int) -> int:
#     return a+b
# print(add.__annotations__)

# def calculate_bill(units):
#     if units <=100:
#        amount = units *2
#     elif units<=200:
#        amount = 100*2+(units-100)
#     else:
#         amount = 100*2+100*4+(units-200*6)
#     return amount+100
# units =int(input("enter units:"))
# bill = calculate_bill(units)
# print("bill", bill)

# def student_system():
#  #200 lines
#  #input
#  #validation
#  #calculation
#  #database
#  #printing 

# better 
# def get_student():
# def validate_student():
# def calculate_student():
# def save_student():
# def disdplay_student():
```

### How to read these examples

The leading `#` makes a line a **comment**. Python displays or executes none of the commented lines above. The explanations below describe what the code would do if the relevant code lines were uncommented and, where necessary, corrected as noted. Source line numbers are included to help find each example in the file.

### Example 1: Printing names (source lines 1-3)

**Purpose and behavior:** Shows three calls to `print`. If uncommented, it prints `Roopa`, `Sakshi`, and `kavya`, each on a new line.

- `print("Roopa")`, `print("Sakshi")`, and `print("kavya")` each display the text inside quotation marks.
- Parentheses contain the argument passed to the `print` function.

**Example output:**

```text
Roopa
Sakshi
kavya
```

### Example 2: Returning a sum (source lines 5-7)

**Purpose and behavior:** Defines `add(a, b)`, returns the sum, and calls it with 2 and 3. The return value is not printed or stored, so uncommenting these lines by themselves displays nothing.

- `def add(a,b):` defines a function with parameters `a` and `b`.
- `return a+b` calculates and gives back the sum.
- `add (2,3)` passes the arguments 2 and 3. Because no `print` uses the returned value, the result `5` is not shown.

**Important concept:** `return` gives a value to the caller; it does not automatically display it. `print(add(2, 3))` would display `5`.

### Example 3: Welcoming several names (source lines 9-13)

**Purpose and behavior:** Defines a function that accepts a name and prints a welcome message, then calls it three times.

- `def welcome(name):` defines the function and its `name` parameter.
- `print("welcome", name)` prints the word `welcome` and the supplied name, separated by a space.
- Each `welcome("...")` line calls the same function with a different string argument.

**Output if uncommented:**

```text
welcome Roopa
welcome nidi
welcome Shree
```

### Example 4: A function without parameters (source lines 15-17)

**Purpose and behavior:** Defines and calls `greet`, which prints `hello`.

- `def greet():` has empty parentheses because the function needs no input.
- The indented `print` runs when the function is called.
- `greet()` calls the function.

**Output:** `hello`

### Example 5: A welcome function with a fixed message (source lines 19-21)

**Purpose and behavior:** Defines a no-parameter function that always prints `welcome to nighan2 labs`, then calls it. The text is fixed in the function; the caller cannot supply a name.

- `def welcome():` defines the function without parameters.
- `print(...)` displays the fixed message.
- `welcome()` runs the function.

**Output:** `welcome to nighan2 labs`

### Example 6: Welcoming one supplied name (source lines 23-25)

**Purpose and behavior:** Another `welcome` example. It receives a name and prints it with `welcome`. It is separate from Example 5; if both definitions are uncommented in the same file, the later definition replaces the earlier function named `welcome`.

- The parameter `name` receives `"Roopa"` from the function call.
- The function prints `welcome Roopa`.

### Example 7: Printing a sum inside a function (source lines 27-29)

**Purpose and behavior:** Adds two numbers and prints the result inside the function. It does not return the sum.

- `def add(a,b):` defines the function.
- `print(a+b)` calculates and displays the sum.
- `add(10,20)` calls it, so its output is `30`.

**Difference from Example 2:** That example returns the sum but does not print it. This example prints it but has no `return` statement.

### Example 8: Printing and returning the sum (source lines 33-37)

**Purpose and behavior:** Prints the sum inside `add`, returns it, stores it in `result`, and prints it again.

- `print(a+b)` displays `30` during the function call.
- `return a+b` then sends `30` back to the caller.
- `result = add(10,20)` stores that returned value.
- `print(result)` displays the stored value a second time.

**Output:**

```text
30
30
```

### Example 9: Returning a value without calling the function (source lines 39-41)

**Purpose and behavior:** Defines `test`, but never calls it. The separate print statement displays `Hello`. The `return 10` line does not run unless `test()` is called.

- `def test():` creates a function.
- `return 10` would return the integer 10 when called.
- `print("Hello")` is outside the function and runs when uncommented.

**Output as written (if uncommented):** `Hello`

### Example 10: Returning three results (source lines 43-49)

**Purpose and behavior:** Calculates a sum, difference, and product; returns all three; assigns them to `X`, `Y`, and `Z`; and prints them.

- `return a+b, a-b, a*b` returns three values as a tuple.
- `calculate(10,5)` produces `(15, 5, 50)`.
- `X, Y, Z = ...` unpacks those three values into three variables.
- The three `print` calls display them one per line.

**Output:**

```text
15
5
50
```

### Example 11: A default parameter value (source lines 51-54)

**Purpose and behavior:** Demonstrates a default name. Calling `greet()` uses `"Roopa"`; supplying a name uses that name instead.

- `name="Roopa"` gives the parameter a default value.
- `greet()` uses the default and prints `hello Roopa`.
- `greet("arati")` passes an argument that replaces the default and prints `hello arati`.

**Output:**

```text
hello Roopa
hello arati
```

### Example 12: Positional arguments (source lines 56-58)

**Purpose and behavior:** Takes a student's name and age and prints both.

- `name` and `age` are parameters.
- `student("Roopa",20)` passes two positional arguments. Their positions determine which parameter receives which value.
- The function prints `Roopa 20`.

### Example 13: Invalid calls and undefined names (source lines 60-61)

**Purpose:** These lines appear to demonstrate keyword arguments and variable names, but they do not have a matching function definition in this example.

- `students(age =21,name ="Roopa")` calls `students`, but the file does not define a function with that name. If uncommented as-is, it raises `NameError` at this line.
- `print(name, age)` also uses names that were not assigned in this scope. It would also fail if execution reached it.

**Problem:** The earlier example defines `student`, singular, and its variables are local to the function. A function's parameter names are not automatically available outside the function. This fragment should not be treated as a working example.

### Example 14: Mixing positional and keyword arguments (source lines 63-65)

**Purpose and behavior:** Passes a student's name, age, and course to a function and prints them.

- `student(name, age, course)` defines three parameters.
- `student("Roopa", age=21, course="BCA")` passes the first value positionally and identifies the other two by parameter name.
- The call prints `Roopa 21 BCA`.

**Keyword argument:** An argument written with its parameter name, such as `age=21`, making its destination explicit.

### Example 15: Accepting any number of positional values (source lines 67-75)

**Purpose and behavior:** Adds however many numbers are supplied.

- `def add(*numbers):` uses `*numbers` to collect extra positional arguments into a tuple named `numbers`.
- `total = 0` starts an accumulator: a variable that keeps a running result.
- `for number in numbers:` repeats the indented body once for each number.
- `total += number` is shorthand for `total = total + number`.
- `return total` gives the final sum back.
- Each `print(add(...))` calls the function with a different number of arguments and displays its result.

**Output:**

```text
30
60
15
```

**Real-world analogy:** It is like adding all the prices in a shopping basket, regardless of how many items are in it.

### Example 16: Accepting keyword details (source lines 77-80)

**Purpose and behavior:** Collects named arguments into a dictionary and prints that dictionary.

- `def student(**details):` uses `**details` to collect keyword arguments into a dictionary.
- `print(details)` displays that dictionary.
- The call supplies `name`, `age`, and `course` as keyword arguments.

**Typical output:**

```text
{'name': 'Roopa', 'age': 21, 'course': 'BCA'}
```

### Example 17: An incomplete function-header fragment (source lines 82-83)

**Purpose:** Appears to list several parameter styles: a required parameter `a`, a defaulted parameter `b=10`, extra positional arguments `*args`, and extra keyword arguments `**kwargs`.

**Problem:** The next line is `pass def test():` on the same line. This is invalid Python syntax: a new `def` statement cannot be placed there after `pass`, and the apparent `test` function has no body. Since both source lines are comments, this syntax error does not affect running `function.py` as it is.

- **`pass`:** A placeholder statement that does nothing. It can serve as a function body while code is unfinished, but it must be placed correctly.
- **`*args`:** Collects additional positional arguments.
- **`**kwargs`:** Collects additional keyword arguments.

### Example 18: A local variable (source lines 85-88)

**Purpose and behavior:** Creates `X` inside `test` and prints it from inside the same function.

- `X=10` assigns 10 to a local variable, one that exists within the function.
- `print(X)` can use it because it is inside that function.
- `test()` calls the function and prints `10`.

**Output:** `10`

### Example 19: Reading a global variable (source lines 90-93)

**Purpose and behavior:** Defines `X` outside the function, then reads it inside the function.

- `X = 100` creates a module-level (global) variable.
- `print(X)` inside `test` reads the global value; it does not assign a new value.
- `test()` calls the function, which prints `100`.

### Example 20: Changing a global variable (source lines 96-101)

**Purpose and behavior:** Increases the global `count` by one.

- `count = 0` creates a global variable.
- `global count` tells Python that the function intends to use and change the global variable rather than create a local one.
- `count += 1` increases the value by one.
- `increment()` changes it from 0 to 1; `print(count)` displays the new value.

**Output:** `1`

### Example 21: Trying to use a local variable outside its function (source lines 105-108)

**Purpose:** Shows a variable-scope mistake.

- `X=10` is local to `test`.
- `test()` creates that local variable and then finishes.
- `print(X)` outside the function cannot access the local `X`.

**Problem:** If uncommented, the last line raises `NameError` because `X` is not defined in the outer scope. A local variable is like a name on a note kept inside one room: code outside that room cannot see it.

### Example 22: Calling one function from another (source lines 110-116)

**Purpose and behavior:** `display` calls `add`, stores its returned sum, and prints it.

- `add(a, b)` returns `a+b`.
- `display()` calls `add(10,20)` and saves the returned `30` in the local variable `result`.
- `print(result)` displays the result.
- `display()` starts this sequence.

**Output:** `30`

### Example 23: Multiplying with a function (source lines 118-121)

**Purpose and behavior:** Multiplies 5 by 4 and prints 20.

- `multiply(a,b)` returns `a*b`.
- `multiply(5,4)` supplies the arguments.
- `result = ...` stores the returned product.
- `print(result)` displays it.

### Example 24: Passing a function to another function (source lines 123-127)

**Purpose and behavior:** Passes `square` to `process`, which calls the supplied function with a value.

- `square(x)` returns `x*x`.
- `process(function, value)` receives a function as its first argument and a value as its second.
- `function(value)` calls whichever function was passed in.
- `process(square,5)` passes the function itself as `function` and the number 5 as `value`.
- The result is `square(5)`, or 25, which `print` displays.

**Important difference:** `square` is passed without parentheses, so it is passed as a function. `square(5)` would call it immediately.

### Example 25: A lambda function (source lines 129-130)

**Purpose and behavior:** Creates a short function that squares one value and prints the result for 5.

- `lambda x: x*x` creates a small anonymous function (a function without a `def` name).
- Assigning it to `square` gives it a usable variable name.
- `square(5)` returns 25.

**Output:** `25`

### Example 26: Using `map` with a tuple and lambda (source lines 132-134)

**Purpose and behavior:** Doubles every number in a tuple and creates a list from the results.

- `numbers = (1,2,3,4)` creates a tuple.
- `lambda x: x*2` describes the operation to perform on each item.
- `map(..., numbers)` applies that operation to each tuple value.
- `list(...)` collects the mapped results into a list.
- `print(result)` displays the list.

**Output:**

```text
[2, 4, 6, 8]
```

### Example 27: A recursive countdown (source lines 136-141)

**Purpose and behavior:** Prints a number and calls itself with a smaller number until it reaches zero.

- `countdown(n)` receives the current number.
- `if n == 0:` checks the stopping condition, also called the base case.
- `return` with no value stops that function call when `n` is zero.
- Otherwise, `print(n)` displays the current number.
- `countdown(n-1)` calls the same function with one less.
- `countdown(5)` starts the sequence.

**Output:**

```text
5
4
3
2
1
```

The program does not print `0`: it returns as soon as `n` becomes zero.

### Example 28: A docstring (source lines 143-148)

**Purpose and behavior:** Gives a function a short description and prints that description.

- The triple-quoted text inside the function is a **docstring**, a description stored with the function.
- `return a+b` returns the sum.
- `add.__doc__` accesses the function's docstring.
- `print(add.__doc__)` displays `return the sum of two numbers ` (the text includes a trailing space in the source).

**Note:** The example does not call `add`; it only prints the description.

### Example 29: Function annotations (source lines 150-152)

**Purpose and behavior:** Adds type hints to the parameters and return value, then prints the function's annotations.

- `a: int` and `b: int` suggest that the parameters should be integers.
- `-> int` suggests that the function returns an integer.
- `return a+b` performs the addition.
- `add.__annotations__` accesses the annotation information stored on the function.

**Typical output:**

```text
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

**Important concept:** These annotations describe intended types; Python does not automatically force every passed value to be an integer.

### Example 30: Calculating an electricity bill (source lines 154-164)

**Purpose and behavior:** Reads units, chooses a formula based on the unit count, adds a fixed 100 charge, and prints the bill.

- `calculate_bill(units)` defines a function receiving the number of units.
- `if units <=100:` selects the first formula for 100 units or fewer: `units * 2`.
- `elif units<=200:` is checked if the first condition is false, and selects a second formula up to 200 units: `100*2 + (units-100)`.
- `else:` handles values above 200.
- `return amount+100` adds a fixed 100 to the amount calculated in the selected branch.
- `units = int(input(...))` reads and converts the unit count.
- `bill = calculate_bill(units)` calls the function.
- `print("bill", bill)` displays the result.

**Problem in the `else` formula:** The source says `100*2+100*4+(units-200*6)`. Because multiplication happens before subtraction, Python evaluates the final part as `units - 1200`, not `(units - 200) * 6`. As a result, values above 200 can produce an incorrect, even negative, bill. For example, at 250 units the code calculates `200 + 400 + (250 - 1200) + 100`, which is `-250`. This guide reports the existing calculation; it does not change the source.

**Input/output example for the source as written:**

```text
enter units:250
bill -250
```

### Example 31: A proposed student-system outline (source lines 166-172)

**Purpose:** The comments list possible responsibilities for a student system: input, validation, calculation, database work, and printing.

- `def student_system():` is itself commented out, so no function is defined.
- The indented `#200 lines`, `#input`, and other notes are comments within the commented example. They are not working code or implemented features.

**What the design idea means:** A large program can be easier to understand when divided into smaller steps, each with one job.

### Example 32: Suggested smaller student functions (source lines 174-179)

**Purpose:** Suggests breaking a student system into functions to get, validate, calculate, and save student information, and to display it.

- `# better` is just a comment.
- The following lines are suggested function headers, but each has a leading `#` and so is not defined by Python.
- `disdplay_student` is spelled `disdplay` in the file; this is likely a spelling mistake in the suggested name.

**Problem if uncommented:** These `def` lines have no function bodies. Python requires an indented body after each function header, so uncommenting them as-is would cause syntax/indentation errors. No student system is implemented in this file.

### Important concepts in `function.py`

- **Comment (`#`):** Text Python ignores. All examples in this file are commented.
- **Function (`def`):** A named, reusable block of code.
- **Parameter / argument:** A parameter is named in a function definition; an argument is the value supplied when calling it.
- **Positional / keyword arguments:** Positional values match by order; keyword values match by parameter name.
- **Default parameter:** A value used if the caller leaves that argument out.
- **`return` and `print`:** `return` gives a value back; `print` displays text or values. They do different jobs.
- **`*args` and `**kwargs`:** Collect extra positional arguments into a tuple and extra keyword arguments into a dictionary.
- **Loop:** `for` repeats a block for items in a collection.
- **Local and global variables:** A local variable belongs to a function call; a global variable is defined outside functions. `global` allows a function to assign to the global variable.
- **Lambda:** A compact way to write a small function.
- **Recursion:** A function calling itself. It needs a stopping condition so calls do not continue forever.
- **Docstring:** A string describing a function.
- **Annotation:** A type hint attached to a parameter or return value.
- **`map`:** Applies a function to each item in an iterable such as a tuple.
- **`list`:** Builds a list from values, including results produced by `map`.

---

## Quick Revision

These are the main Python ideas actually shown in the files.

- **Variables:** Names such as `marks`, `number`, and `discount` store values.
- **Data types:** The examples use integers (`int`), decimal numbers (`float`), strings (text), Booleans (`True`/`False`), tuples, lists, and dictionaries.
- **Input and output:** `input()` reads text from the user; `print()` displays results.
- **Type conversion:** `int()` converts suitable text to a whole number; `float()` converts suitable text to a decimal number.
- **Operators:** `+`, `-`, `*`, `/`, `//`, `%`, and `+=` perform arithmetic. `==`, `>=`, and `<=` compare values.
- **Conditions:** `if`, `elif`, and `else` choose which code runs. `and`, `or`, and `not` combine or reverse truth values.
- **Loops:** `for` repeats a block for each item in a collection.
- **Functions:** `def` creates a reusable block; calling the function runs it.
- **Parameters and arguments:** Parameters are function inputs named in its definition; arguments are the actual values supplied by a call.
- **`return`:** Sends a result from a function to its caller. It is not the same as printing that result.
- **Built-in functions and methods:** The files use `input`, `print`, `int`, `float`, `list`, `map`, and methods such as `.strip()`, `.lower()`, and `.get()`.
- **Lists:** Ordered collections in square brackets; used for the required skills.
- **Tuples:** Ordered collections in parentheses; used for fixed operator choices and multiple returned values.
- **Dictionaries:** Key/value collections in braces; used to store number checks and map experience labels to categories.
- **Strings:** Text values in quotation marks; string comparisons in these programs are exact unless the program explicitly normalizes the text.
- **Exceptions:** `raise`, `try`, and `except` demonstrate reporting and handling specific errors in the calculator.
- **Modules/imports:** No Python file in this set imports a module.
- **Scope:** Local and global variables are demonstrated in the commented examples in `function.py`.
- **Lambda and `map`:** A lambda is used as a small transformation function, and `map` applies it to each item.
- **Recursion:** `countdown` demonstrates a function calling itself until it reaches a stopping condition.
- **Docstrings and annotations:** The commented examples show a function description and type hints.
- **Input validation:** Most scripts assume their inputs can be converted and are within sensible ranges. The calculator handles some operation errors, but its numeric conversions occur before its `try` block.
