# Python Continue Statement

for i in range(1, 11):
    if i == 6:
        continue
    print(i, end=" ")

print()

# Skipping specific characters in a string
for char in "GeeksforGeeks":
    if char == "e":
        continue
    print(char, end=" ")


# Skipping Specific Values: Ignore certain values without breaking the loop.
# Filtering Data Dynamically: Exclude elements that do not meet a condition.
# Optimizing Loop Performance: Avoid unnecessary computations for some iterations.