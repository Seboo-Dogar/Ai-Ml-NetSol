# Python While Loop

i = 0
while i < 5:
    print(i)
    i += 1
print() # Move to next line

count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")
print()

#------------------------------
# Infinite while Loop
# Uncommenting the below code will cause an infinite loop

# age = 28
# # the test condition is always True
# while age > 19:
#     print('Infinite Loop')

#-----------------------------
# while loop with continue statement

# Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print(a[i])
    i += 1
print()

#-------------------------------
#while loop with break statement


i = 0
a = 'geeksforgeeks'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
        
    print(a[i])
    i += 1
print()

#-------------------------------
# while loop with else

i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")
