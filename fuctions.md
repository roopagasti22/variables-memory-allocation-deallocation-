# Python Functions: A Detailed Guide

## 1. Why Do We Use Functions?

Suppose a program needs to print a greeting for several people. We could write the same instruction repeatedly:

```python
print("Hello, Roopa!")
print("Hello, Sakshi!")
print("Hello, Kavya!")
```

This works, but repeated code is harder to update. If the greeting changes, every copy must be changed. A function lets us write a task once and use it whenever we need it.

## 2. What Is a Function?

A function is a named, reusable block of code that performs a particular task. It can receive information, work with that information, and optionally send a result back to the code that called it.

```python
def add(first_number, second_number):
    return first_number + second_number

total = add(2, 3)
print(total)  # 5
```

Here, `add` is the function name. The function receives two numbers and returns their sum.

## 3. What Problems Do Functions Solve?

Functions help us:

- Reuse code instead of copying it.
- Reduce repetition and the chance of inconsistent changes.
- Organize a program into smaller, understandable tasks.
- Test one piece of behavior at a time.
- Maintain code more easily as a program grows.

A good function usually has a clear purpose and a name that describes that purpose, such as `calculate_total` or `display_welcome_message`.

## 4. Defining a Function Versus Calling It

Defining a function tells Python what the function should do. The indented lines form the function body:

```python
def greet():
    print("Hello!")
```

Defining the function does not run its body. To run it, call the function by writing its name followed by parentheses:

```python
greet()
```

When Python reaches `greet()`, it executes the function body. A function can be called more than once.

## 5. Functions Without Parameters

A function does not need to receive any information. A function with empty parentheses is useful when it always performs the same task:

```python
def welcome_to_lab():
    print("Welcome to Nighan2 Labs!")

welcome_to_lab()
```

The parentheses are still required when defining and calling the function, even though there are no parameters.

## 6. Functions With Parameters

Parameters are named inputs listed in a function definition. They let the function work with different values on different calls.

```python
def welcome(name):
    print("Welcome,", name)

welcome("Roopa")
welcome("Nidi")
welcome("Shree")
```

In this example, `name` is a parameter. The values `"Roopa"`, `"Nidi"`, and `"Shree"` are arguments supplied when the function is called.

## 7. Functions With Multiple Parameters

A function can receive multiple inputs. In a normal call, positional arguments are matched to parameters from left to right:

```python
def add(first_number, second_number):
    return first_number + second_number

print(add(10, 20))  # 30
```

The first argument, `10`, is assigned to `first_number`; the second argument, `20`, is assigned to `second_number`.

## 8. Returning a Value

`print()` displays information for a person to see. `return` sends a value from a function back to the code that called it. These are different jobs.

```python
def add_and_display(first_number, second_number):
    print(first_number + second_number)

def add_and_return(first_number, second_number):
    return first_number + second_number

add_and_display(10, 20)  # Displays 30; the function returns None.

result = add_and_return(10, 20)
print(result)  # Displays 30.
```

Use `return` when another part of the program needs to use the result, for example, to store it, compare it, or pass it to another function.

## 9. What Happens After `return`?

When Python executes `return`, it immediately leaves that function and sends the value back to the caller. Any statements later in the same function call are skipped.

```python
def test():
    return 10
    print("This line is never reached")

value = test()
print(value)  # 10
print("This line is outside the function, so it still runs")
```

`return` ends the current function call; it does not stop the entire program.

## 10. Returning Multiple Values

Python lets a function return several values separated by commas. Python packages them into a tuple, which can be unpacked into separate variables:

```python
def calculate(first_number, second_number):
    return (
        first_number + second_number,
        first_number - second_number,
        first_number * second_number,
    )

sum_result, difference, product = calculate(10, 5)
print(sum_result)  # 15
print(difference)  # 5
print(product)  # 50
```

The number of variables on the left must match the number of returned values when unpacking this way.

## 11. Default Parameter Values

A parameter can have a default value. Python uses that value when the caller leaves out the corresponding argument.

```python
def greet(name="Roopa"):
    print("Hello,", name)

greet()          # Hello, Roopa
greet("Arati")   # Hello, Arati
```

Defaults are useful when one value is common but callers should still be able to provide another. In a function definition, parameters without defaults must come before parameters with defaults. For example, `def greet(name, message="Hello"):` is valid.

Avoid using a mutable object such as a list as a default value when you intend to create a fresh object for each call. Default values are created when the function is defined, not each time it is called.

## 12. Positional Arguments

Positional arguments are assigned to parameters according to their position in the call:

```python
def show_student(name, age):
    print(name, age)

show_student("Roopa", 20)
```

Here, `"Roopa"` is assigned to `name`, and `20` is assigned to `age`. The order matters for positional arguments.

## 13. Keyword Arguments

Keyword arguments identify a parameter by name. This makes a call easier to read, and the keyword arguments can be written in a different order from the parameter definition:

```python
def show_student(name, age):
    print(name, age)

show_student(age=21, name="Roopa")
```

The parameter names must be spelled correctly. A parameter must not be given a value more than once in the same call.

## 14. Combining Positional and Keyword Arguments

Positional and keyword arguments can be used together. Positional arguments must come before keyword arguments:

```python
def show_student(name, age, course):
    print(name, age, course)

show_student("Roopa", age=21, course="BCA")
```

This call is invalid:

```python
show_student(name="Roopa", 21, course="BCA")
```

The positional argument `21` appears after a keyword argument. Python cannot match that call unambiguously. Use `age=21` or move `21` before the keyword arguments.

## 15. `*args`: A Variable Number of Positional Arguments

Use `*args` when a function should accept any number of additional positional arguments. The name `args` is a convention; the `*` is what collects the extra values into a tuple.

```python
def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_numbers(10, 20))          # 30
print(add_numbers(10, 20, 30))      # 60
print(add_numbers(1, 2, 3, 4, 5))  # 15
```

The function also works when no extra positional arguments are provided: `numbers` will be an empty tuple.

## 16. `**kwargs`: A Variable Number of Keyword Arguments

Use `**kwargs` when a function should accept additional keyword arguments. The extra named values are collected into a dictionary. The name `kwargs` is a convention; the `**` performs the collection.

```python
def show_student_details(**details):
    print(details)

show_student_details(name="Roopa", age=21, course="BCA")
# {'name': 'Roopa', 'age': 21, 'course': 'BCA'}
```

This is helpful when the set of named options may vary. Inside the function, `details` can be accessed like any other dictionary.

## 17. Combining Parameter Types

A function can combine required parameters, default values, `*args`, keyword-only parameters, and `**kwargs`. Their order in the definition matters:

```python
def example(required, default_value=10, *args, option=False, **kwargs):
    print(required)
    print(default_value)
    print(args)
    print(option)
    print(kwargs)

example("item", 20, "extra", option=True, color="blue")
```

In this example, `required` is required, `default_value` has a default, additional positional values are collected in `args`, `option` is keyword-only, and additional keyword values are collected in `kwargs`.

## 18. Local Scope and Global Scope

Scope describes where a name can be accessed.

A variable assigned inside a function is local to that function by default:

```python
def show_value():
    value = 10
    print(value)

show_value()  # 10
```

A variable defined outside a function is global to its module. A function can read that name if there is no local name with the same spelling:

```python
value = 100

def show_global_value():
    print(value)

show_global_value()  # 100
```

Although reading a global value is allowed, functions are usually easier to reuse and test when required values are passed in as parameters.

## 19. The `global` Keyword

If a function assigns to a name, Python treats that name as local unless told otherwise. The `global` keyword tells Python that an assignment should update a module-level name:

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1
```

Use `global` sparingly. Shared global state can make behavior harder to follow and test. For reusable code, it is often clearer to pass a value into a function and return the updated value:

```python
def increment(count):
    return count + 1

count = increment(0)
```

## 20. A Local Variable Is Not Available Outside Its Function

A local variable exists only while the function is running and cannot normally be accessed by code outside it:

```python
def create_value():
    value = 10

create_value()
print(value)  # Raises NameError: value is not defined here.
```

To use a value after a function finishes, return it and assign the result:

```python
def create_value():
    value = 10
    return value

result = create_value()
print(result)  # 10
```

## 21. Functions Can Call Other Functions

Functions can be combined to divide a larger task into smaller steps. One function can call another and use its returned value:

```python
def add(first_number, second_number):
    return first_number + second_number

def display_total():
    result = add(10, 20)
    print(result)

display_total()  # 30
```

Notice that `result` is created inside `display_total`, so it is local to that function. The `add` function returns the calculation result to its caller.

A larger program might follow a sequence such as:

1. Validate the input.
2. Calculate the result.
3. Save the result.
4. Display the result.

Each step can be placed in a well-named function. This makes the program easier to read, test, and change.










