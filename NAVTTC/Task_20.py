#User defined functions in Python:

def fun():
    print("Hello this is a user defined function")
    
fun()

#-------------------
# Function Arguments
def fun(name):
    print("Hello " + name)

fun("Seboo")
print("-----------")

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))
print("--------------")


#-------------------
# Default Arguments

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)
myFun(10, 20)
print("----------")

#-------------------
# Keyword Arguments
# the order doesn’t matter.

def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')
print("------------------")

#-------------------
# Positional Arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Olivia", 27)

print("\nCase-2:")
nameAge(27, "Olivia")
print("-------------------")

#-------------------------
# Arbitrary Arguments

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')
print("------------------------")

#----------------------------
# Function within Functions
def outerFun(text):
    def innerFun():
        print("inner function print :", text)
    innerFun()

outerFun("Hello, I am a function within a function")
print("-----------------------------")

#--------------------------------
# Anonymous Functions
# Lambda functions are anonymous functions that can have any number of arguments but only one expression.
# an anonymous function means that a function is without a name.

def square(x):
    return x * x

# Lambda function for the same purpose
square_lambda = lambda x: x * x
print(square(5))  # Output: 25
print(square_lambda(5))  # Output: 25
print("-----------------")

#--------------------------------
# Return Statement in Function
def add(a, b):
    return a + b

result = add(10, 20)
print("The sum is:", result)

def sq_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(sq_value(2))
print(sq_value(-4))
print()

#----------------------------------
# Pass by Reference and Pass by Value

def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   

def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)
print("---------------------")

#----------------------------
# Recursive Functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))  # Output: 120