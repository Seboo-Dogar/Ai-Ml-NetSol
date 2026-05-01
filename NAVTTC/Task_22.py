# Create a tuple
fruits = ("apple", "banana", "cherry", "mango")

# Tuples are:

# Ordered - They maintain the order of elements.
# Immutable - They cannot be changed after creation.
# Allow duplicates - They can contain duplicate values.

# Access elements
print(fruits[0])     # First element
print(fruits[-1])    # Last element

# Slicing
print(fruits[1:3])   # From index 1 to 2

numbers = (10, 20, 30)

# Convert to list to modify
temp = list(numbers)
temp.append(40)

# Convert back to tuple
numbers = tuple(temp)

print(numbers)

# Packing
person = ("Ali", 22, "Student")

# Unpacking
name, age, role = person

print(name)
print(age)
print(role)

colors = ("red", "green", "blue")

# Direct loop
for color in colors:
    print(color)

# Using index
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")

nums = (1, 2, 3, 2, 4, 2)

print(nums.count(2))   # Count occurrences
print(nums.index(3))   # First index of 3

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Access element
print(matrix[1][2])  # 6

# Traverse nested tuple
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# Swap two values using tuple unpacking
a = 5
b = 10

a, b = b, a

print("a =", a)
print("b =", b)