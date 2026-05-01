# Exercise on Set data type in Python

# create a set of integer type
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# create a set of string type
my_set2 = {"apple", "banana", "cherry"}
print("Original set:", my_set2)

# create a set of mixed data types
my_set3 = {1, "hello", 3.14, True}
print("Original set:", my_set3)

# Create an Empty Set in Python

# create an empty set
empty_set = set()
print("Empty set:", empty_set)
# check data type of empty_set
print("Data type of empty_set:", type(empty_set))

# create an empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)
# check data type of empty_dict
print("Data type of empty_dict:", type(empty_dict))
print()


# Duplicate Items in a Set
# a set cannot contain duplicates. If you try to add duplicate items to a set, it will only keep one instance of that item.
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)   # {8, 2, 4, 6} 
print()


# Add Items to a Set in Python
numbers = {21, 34, 54, 12}
print('Initial Set:',numbers)

# using add() method
numbers.add(32)
print('Updated Set:', numbers) 
print()


# Update Python Set
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

# using update() method
companies.update(tech_companies)

print(companies)
print()


# Remove an Element from a Set
fruits = {'apple', 'banana', 'cherry', 'orange'}
# using remove() method
fruits.remove('banana')
print(fruits)
# using discard() method
fruits.discard('orange')
print(fruits)
# using pop() method
fruits.pop() # removes and returns an arbitrary element from the set
print(fruits)
print()


# Built-in Functions with Set
numbers = {8, 2, 9, 1, 7, 3, 4, 5, 6}
print("Length of the set:", len(numbers))  # Output: 9
print("Maximum value in the set:", max(numbers))  # Output: 9
print("Minimum value in the set:", min(numbers))  # Output: 1
print("Sorted set:", sorted(numbers))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Sum of the set:", sum(numbers))  # Output: 45
print("Enumerated set:")
for i, value in enumerate(numbers): # enumerate() function adds a counter to an iterable and returns it as an enumerate object
    print(f"Index: {i}, Value: {value}")

all(x > 0 for x in numbers)  # Output: True
any(x > 8 for x in numbers)  # Output: True 
print("Set after clearing:", numbers.clear())  # Output: None


# Iterate Over a Set in Python
fruits = {"Apple", "Peach", "Mango"}

# for loop to access each fruits
for fruit in fruits: 
    print(fruit)





# Python Set Operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# Union of two sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# perform union operation using | operator
union_set2 = set1 | set2
print("Union of set1 and set2 (using |):", union_set2)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of two sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)  # Output: {4, 5}
# perform intersection operation using & operator
intersection_set2 = set1 & set2
print("Intersection of set1 and set2 (using &):", intersection_set2)  # Output: {4, 5}

# Difference of two sets
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)  # Output: {1, 2, 3}
# perform difference operation using - operator
difference_set2 = set1 - set2
print("Difference of set1 and set2 (using -):", difference_set2)  # Output: {1, 2, 3}


# Symmetric Difference of two sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}
# perform symmetric difference operation using ^ operator
symmetric_difference_set2 = set1 ^ set2
print("Symmetric Difference of set1 and set2 (using ^):", symmetric_difference_set2)  # Output: {1, 2, 3, 6, 7, 8}



#Check if two sets are equal
# first set
A = {1, 3, 5}

# second set
B = {3, 5, 1}

# perform difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')