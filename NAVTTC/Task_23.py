# Exercise on String data type in Python: 

# create a string using double quotes
greeting = "Hello, World!"
print(greeting)

# create a string using single quotes
name = 'Alice'
print(name)
print()


# Access String Characters in Python
message = "Python Programming"

# Accessing characters using indexing
print(message[0])  # Print the first character
print(message[8])  # Print the ninth character
print(message[-6])  # Print the sixth character from the end
print(message[0:6]) # access character from zeroth index to 6th index
print("-----------------------------")


# In Python, strings are immutable. That means the characters of a string cannot be changed. For example,
message = 'Hola Amigos'

# message[0] = 'A' 
# print(message)


# However, we can assign the variable name to a new string. For example,
message = 'Hola Amigos'

# assign new string to message variable
message = 'Hello Friends'
print(message); # prints "Hello Friends"

# Python Multiline String
multiline_string = """This is a multiline string.
It can span multiple lines."""
print(multiline_string)
print()


# -------------------------------------
# Python String Operations
str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)


# Join Two or More Strings
combined_string = str1 + " " + str2
print(combined_string)
print()

# Iterate Through a Python String 
name = "Seboo"
for char in name:
    print(char)

# Python String Length
sentence = "Python is great!"
length = len(sentence)
print("The length of the sentence is:", length)


# String Membership Test
text = "Hello, world!"
print("Hello" in text)  # True
print("Python" in text)  # False
print("H" in text)      # True
print("h" in text)      # False (case-sensitive)
print()


# Methods of Python String
text = "Hello, World!"
print(text.upper())  # Convert to uppercase
print(text.lower())  # Convert to lowercase
print(text.replace("World", "Python"))  # Replace a substring
print(text.split(","))  # Split the string by comma
print(text.strip())   # Remove leading and trailing whitespace
print(text.startswith("Hello"))  # Check if the string starts with "Hello"
print(text.isnumeric())  # Check if the string is numeric
print(text.index("World"))  # Find the index of "World" in the string



# Escape Sequences in Python
print("Hello, World!")  # Normal string
print("Hello, \nWorld!")  # Newline character
print("Hello, \tWorld!")  # Tab character
print("Hello, \"World\"!")  # Double quote character
print("Hello, 'World'!")  # Single quote character


# Python String Formatting (f-Strings)
name = "Aslam"
age = 55
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)