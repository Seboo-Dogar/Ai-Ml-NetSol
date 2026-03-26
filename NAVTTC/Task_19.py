# Exercise on various looping techniques in Python: 

# Using enumerate()
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

print()

words = ['The', 'Big', 'Bang', 'Theory']

for index, value in enumerate(words):
    print(index, value)
print("----------------------")

#-----------------------------------------------
# Using zip()
# zip() function combines two or more containers and iterates over them in parallel. The loop stops at the length of the shortest container.
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

print("----------------------")
#--------------------------------------------
# Using items()
# items() allows you to loop through a dictionary and access both its keys and values simultaneously.
person = {"name": "Alice", "age": 25, "city": "New York"}

for key, value in person.items():
    print(f"{key}: {value}")
print("----------------------")

#--------------------------------------------
# Using sorted()
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

for n in sorted(numbers):
    print(n, end=' ')

print("\nSorted list without duplicates:")
for n in sorted(set(numbers)):
    print(n, end=" ")
print()

#--------------------------------------------
# Using reversed()
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]

for n in reversed(nums):
    print(n, end=' ')
print()

