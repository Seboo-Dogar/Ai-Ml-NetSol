# Python Exception Handling
# Exception handling is a mechanism to handle errors gracefully in Python. It allows you to write code that can handle exceptions (errors) without crashing the program.

# Python try...except Block
try:
    # Code that may raise an exception
    num1 = 10
    num2 = 0
    result = num1 / num2  # This will raise a ZeroDivisionError
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



# Catching Specific Exceptions in Python
try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])
except ZeroDivisionError:
    print("Denominator cannot be 0.") 
except IndexError:
    print("Index Out of Bound.")
# Output: Index Out of Bound



# Python try with else clause
try:
    num1 = 10
    num2 = 5
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("The result is:", result)

    

# Python try with finally clause
try:   
    num1 = 10
    num2 = 0
    result = num1 / num2

    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This will always execute.")