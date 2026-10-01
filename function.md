# Python Functions: A Detailed Guide

## 1. Why do we use functions?

Suppose we want to print the same greeting for several people. Without functions, we would repeat the same code again and again:

```python
print("Roopa")
print("Sakshi")
print("Kavya")
```

This works, but it is repetitive and hard to maintain. If the greeting changes, we must update every line manually. A function lets us write a task once and reuse it whenever needed.

## 2. What is a function?

A function is a reusable block of code that performs a specific task. It can accept inputs, process them, and optionally return a result.

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # 5
```

Here:
- `add` is the function name
- `a` and `b` are parameters
- `2` and `3` are arguments
- `return` sends the result to the caller

Another example:

```python
def welcome(name):
    print("Welcome", name)

welcome("Roopa")
welcome("Nidhi")
welcome("Shree")
```

This function can be called with different names without rewriting the logic.

## 3. What problems do functions solve?

Functions help us:

- reuse code instead of copying it
- reduce repetition
- organize large programs into smaller tasks
- make code easier to read and maintain
- test each part of the program separately

A good function has a clear purpose and a meaningful name, such as:

- `calculate_total()`
- `display_welcome_message()`
- `validate_age()`

## 4. Defining a function vs calling a function

Defining a function tells Python what the function should do, but it does not execute the code immediately.

```python
def greet():
    print("Hello!")
```

This defines the function. To run it, we must call it:

```python
greet()
```

When Python reaches `greet()`, it executes the body of the function.

## 5. Functions without parameters

A function does not need to receive any value.

```python
def welcome_to_lab():
    print("Welcome to Nighan2 Labs!")

welcome_to_lab()
```

Even without parameters, the parentheses are still required both in the definition and in the call.

This is useful when the task is always the same.

## 6. Functions with parameters

Parameters are variables declared inside the function definition.

```python
def welcome(name):
    print("Welcome", name)

welcome("Roopa")
```

Here:
- `name` is a parameter
- `"Roopa"` is an argument passed to the function

Different arguments can be passed on different calls.

## 7. Functions with multiple parameters

A function may accept more than one input.

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

The first argument is assigned to `a`, and the second argument is assigned to `b`.

## 8. Returning a value

`print()` only shows a value. It does not send the value back to the program.

`return` is used when the function needs to give a value back to the caller.

### Example using `print()`

```python
def add_and_display(a, b):
    print(a + b)

add_and_display(10, 20)
```

This displays `30`, but the result is not available for further use.

### Example using `return`

```python
def add_and_return(a, b):
    return a + b

result = add_and_return(10, 20)
print(result)
```

This is more useful because the result can be stored, compared, or passed to another function.

## 9. What happens after `return`?

When Python executes `return`, it leaves the function immediately and sends the value back to the caller.

```python
def test():
    return 10
    print("This line is never reached")

value = test()
print(value)
```

The `print()` after `return` is never executed. `return` ends the current function call, not the whole program.

## 10. Returning multiple values

A function can return more than one value.

```python
def calculate(a, b):
    return a + b, a - b, a * b

sum_result, difference, product = calculate(10, 5)
print(sum_result)  # 15
print(difference)  # 5
print(product)    # 50
```

Python packs multiple return values into a tuple. We can unpack them into separate variables.

## 11. Default parameter values

A parameter can have a default value.

```python
def greet(name="Roopa"):
    print("Hello", name)

greet()          # Hello Roopa
greet("Arati")  # Hello Arati
```

Default values are useful when one value is usually the same, but the caller can still provide a different value.

Important rule:
- parameters without default values must come before parameters with default values

```python
def greet(name, message="Hello"):
    print(message, name)
```

## 12. Positional arguments

Positional arguments are assigned based on their order.

```python
def student(name, age):
    print(name, age)

student("Roopa", 20)
```

Here:
- `"Roopa"` goes to `name`
- `20` goes to `age`

The order matters.

## 13. Keyword arguments

Keyword arguments are passed by name instead of by position.

```python
def student(name, age):
    print(name, age)

student(age=21, name="Roopa")
```

The order does not matter when we use keyword arguments, as long as the parameter names are correct.

## 14. Combining positional and keyword arguments

Python allows both in the same function call, but positional arguments must appear before keyword arguments.

```python
def student(name, age, course):
    print(name, age, course)

student("Roopa", age=21, course="BCA")
```

This is valid.

This is invalid:

```python
student(name="Roopa", 21, course="BCA")
```

A positional argument cannot come after a keyword argument.

## 15. `*args`: variable number of positional arguments

Sometimes a function must accept any number of positional arguments.

```python
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add(10, 20))
print(add(10, 20, 30))
print(add(1, 2, 3, 4, 5))
```

`*numbers` collects all the extra arguments into a tuple.

This is useful when the number of inputs is not fixed.

## 16. `**kwargs`: variable number of keyword arguments

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def student(**details):
    print(details)

student(name="Roopa", age=21, course="BCA")
```

Output:

```python
{'name': 'Roopa', 'age': 21, 'course': 'BCA'}
```

This is useful when a function needs to accept different named values.

## 17. Combining parameter types

A function can combine different kinds of parameters.

```python
def example(a, b=10, *args, option=False, **kwargs):
    print(a)
    print(b)
    print(args)
    print(option)
    print(kwargs)

example("item", 20, "extra", option=True, color="blue")
```

In this example:
- `a` is a required argument
- `b` has a default value
- `*args` collects extra positional values
- `option` is a keyword-style flag
- `**kwargs` collects extra named values

## 18. Local scope vs global scope

Scope defines where a variable can be used.

### Local variable

```python
def test():
    x = 10
    print(x)

test()
```

The variable `x` exists only inside `test()`.

### Global variable

```python
x = 100

def test():
    print(x)

test()
```

The function can read the global value of `x`.

## 19. The `global` keyword

If a function assigns a new value to a variable, Python treats it as local unless we tell it otherwise.

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1
```

The `global` keyword tells Python to modify the module-level variable instead of creating a separate local variable.

However, global variables can make code harder to test and maintain. It is often better to pass values into functions and return results.

## 20. A local variable is not available outside its function

```python
def create_value():
    value = 10

create_value()
print(value)
```

This raises `NameError` because `value` is local to `create_value()`.

To use the value outside the function, return it:

```python
def create_value():
    value = 10
    return value

result = create_value()
print(result)
```

Now the result is available outside the function.

## 21. Functions can call other functions

One function can call another function.

```python
def add(a, b):
    return a + b

def display_total():
    result = add(10, 20)
    print(result)

display_total()
```

This is useful because large tasks can be divided into smaller, easier parts.

A program may follow this flow:

1. validate input
2. calculate result
3. save data
4. display output

Each step can be implemented as a separate function.

## 22. Function calling flow

```python
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)
```

Flow of execution:
- Python calls `multiply(5, 4)`
- `a` receives `5`
- `b` receives `4`
- the function computes `5 * 4`
- it returns `20`
- the returned value is stored in `result`
- `print(result)` displays `20`

This shows the basic flow of a function call.

## 23. Functions are objects in Python

In Python, functions are treated as first-class objects.

```python
def greet():
    print("Hello")

x = greet
x()
```

Here, `x` refers to the same function object as `greet`. It can be called using `x()`.

This feature allows functions to be assigned, passed, and used dynamically.

## 24. Passing a function to another function

A function can accept another function as an argument.

```python
def square(x):
    return x * x

def process(func, value):
    return func(value)

print(process(square, 5))
```

This is an example of a higher-order function.

A higher-order function is a function that takes another function as an argument or returns a function.

## 25. Lambda functions

A lambda function is an anonymous function written in one line.

```python
square = lambda x: x * x
print(square(5))  # 25
```

Lambda functions are useful for short operations.

Example with `map()`:

```python
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)
```

Output:

```python
[2, 4, 6, 8]
```

Lambda functions are convenient but not ideal for long or complex logic.

## 26. Recursion

A recursive function calls itself.

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)
```

Output:

```python
5
4
3
2
1
```

Recursion is used for problems such as factorial, Fibonacci, and tree traversal. However, careful base conditions are required to avoid infinite recursion.

## 27. Function documentation

Python allows docstrings to describe what a function does.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add.__doc__)
```

Docstrings help developers understand the purpose of the function quickly.

## 28. Type hints

Type hints tell readers and tools what kind of values a function expects and returns.

```python
def add(a: int, b: int) -> int:
    return a + b
```

This means:
- `a` should be an integer
- `b` should be an integer
- the function returns an integer

Python does not enforce type hints at runtime, but they improve readability and help with IDE support.

## 29. A practical example: electricity bill calculation

```python
def calculate_bill(units):
    if units <= 100:
        amount = units * 2
    elif units <= 200:
        amount = 100 * 2 + (units - 100) * 3
    else:
        amount = 100 * 2 + 100 * 3 + (units - 200) * 5
    return amount + 100

units = int(input("Enter units: "))
bill = calculate_bill(units)
print("Bill:", bill)
```

This is a good example of why functions are useful. Instead of writing all the logic in one block, we divide the logic into a function that can be tested and reused.

Why create a function instead of doing everything in the main program?

- separation of responsibility
- code reuse
- easier testing
- better readability
- easier maintenance

## 30. Function design

A good function usually has:

- a meaningful name
- a single clear purpose
- manageable input parameters
- a clear output or return value

A function should ideally do one task well.

## 31. Do not create giant functions

Avoid writing one huge function that does everything.

### Bad design

```python
def student_system():
    # 200 lines of code
    # input
    # validation
    # calculations
    # database logic
    # printing
    pass
```

This is hard to understand and maintain.

### Better design

```python
def get_student():
    pass

def validate_student():
    pass

def calculate_student():
    pass

def save_student():
    pass

def display_student():
    pass
```

This follows the principle of single responsibility: each function handles one task.

## 32. Summary

Functions are one of the most important concepts in Python because they:

- reduce repetition
- organize code logically
- make code reusable
- simplify testing and debugging
- help build larger and cleaner programs

A function contains:
- a name
- optional parameters
- a block of code
- optional return value

A well-designed function is clear, efficient, and focused on one job.

In short, functions are the building blocks of structured programming.

