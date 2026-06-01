# Python Custom Exceptions
# In Python, you can create your own custom exceptions by defining a new class that inherits from the built-in Exception class. This allows you to create specific error types that can be used to handle specific situations in your code.


# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")



# Customizing Exception Classes
class InvalidAgeException(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Invalid Age: {self.age}. Age must be at least 18."

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException(input_num)
    else:
        print("Eligible to Vote")
        
except InvalidAgeException as e:
    print("Exception occurred:", e)

