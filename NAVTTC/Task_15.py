#Python For Loops

s = ["Geeks", "for", "Geeks"]
# using for loop with list of strings
for i in s:
    print(i)
print() # Move to next line

#------------------------------
# Iterating over characters of strings

s = "Geeks"

for i in s:
    print(i)
print() 

#-------------------------------
# Using range() with For Loop
# range(start, stop, step)

for i in range(0, 10, 2):
    print(i)
print() 

#-------------------------------
# Continue with For Loop

for i in range(1, 10):
    if i == 5:
        continue
    print(i)
print()

# Prints all letters except 'e' and 's'
for i in 'geeksforgeeks':

    if i == 'e' or i == 's':
        continue
    print(i)
print()

#-----------------------------------
# Break with For Loop

for i in range(10):
    if i == 5:
        break
    print(i)
print() 

for i in 'geeksforgeeks':
    # break the loop as soon it sees 'e'
    # or 's'
    if i == 'e' or i == 's':
        break
    print(i)
print()

#----------------------------------
# Pass Statement with For Loop
#pass is a null statement — it does nothing at all.

for i in range(10):
    if i == 5:
        pass # will implement later
    print(i)
print()

# An empty loop
for i in 'geeksforgeeks':
    pass # will implement later
print(i)

print()

#-----------------------------------
# Else Statement with For Loops
# The else block just after for/while is executed only when the loop is NOT terminated by a break statement.

for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

#-----------------------------------
# Using Enumerate with for loop
# In Python, enumerate() function is used with the for loop to iterate over an iterable while also keeping track of index of each item.

li = ["eat", "sleep", "repeat"]
for index, item in enumerate(li):
    print(index, item)
print()

#------------------------------------
# Nested For Loops

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)