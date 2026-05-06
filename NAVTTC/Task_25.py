# Python Dictionary
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

# Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

# Accessing Items
print(thisdict["brand"])
print(thisdict.get("model"))

# Add Items to a Dictionary
thisdict["color"] = "red"
print(thisdict)

# Remove Dictionary Items
thisdict.pop("model")
print(thisdict)

# using del keyword:
del thisdict["year"]
print(thisdict)

# Change Dictionary Items
# Python dictionaries are mutable (changeable). We can change the value of a specific item by referring to its key name:
thisdict["brand"] = "Chevrolet"
print(thisdict)


# Iterate Through a Dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print()

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)

# Find Dictionary Length
print(len(country_capitals))
countries = {}
print(len(countries))


# Dictionary Membership Test
file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

print(".txt" in file_types)
print(".doc" in file_types)
print(".pdf" in file_types)       # Output: True
print(".mp3" in file_types)       # Output: False
print(".mp3" not in file_types)   # Output: True