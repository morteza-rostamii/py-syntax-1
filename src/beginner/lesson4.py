import copy
# copy values
print("**************\n")

# string:

# single or double quotes:
username = "John Doe"
username2 = 'John Doe'

# triple quotes:
username3 = """John Doe"""
username4 = '''John Doe'''

# print(username3, username4)

# also: F-string:

greeting = F"hello {username}"
# print(greeting) # hello John Doe

# access string index
# print(username[0]) # J
# print(username[-1]) # e
# print(username[2:4]) # hn

# reverse a string
# print(username[::-1])

good: str = "good day"
# string is immutable, so cannot change ERROR
# good[0] =  "$"

# print(good)

# so to edit the string => create a new one
newStr: str = "$" + good[1:]
# print(newStr) # $ood day

# list: 
# ordered and mutable

colors = ["red", "green", "blue"]
# print(colors[0]) # red
# print(colors[-1]) # blue

# list is mutable
colors[0] = "yellow"
# print(colors) # ['yellow', 'green', 'blue']

# append to the end
colors.append("black")
# print(colors) # ['yellow', 'green', 'blue', 'black']

# get last item
last_item = colors.pop()
# print(last_item) # black

# tuples: ordered, immutable
cloths = ("shirt", "pants", "shoes")
# print(cloths[0]) # shirt
# print(cloths[-1]) # shoes

# immutable
# cloths[0] = "hat"

# unpacking of list and tuple

a, b, c = colors
# print(a) # yellow
# print(b) # green
# print(c) # blue

# unpacking of tuple
d, e, f = cloths
# print(d) # shirt
# print(e) # pants
# print(f) # shoes

# dict: unordered, mutable
person = {"name": "John", "age": 30, "city": "New York"}
# print(person["name"]) # John

# print(person.get("ag2e", "age not found"))

# loop a dictionary
# for key in person:
#   print(key, person[key])

# for key, value in person.items():
#   print(key, value)

# Set => unordered, unique values

emails = {"RyTt5@example.com"}

emails.add("xYd0l@example.com")
# can't add a duplicate
emails.add("RyTt5@example.com") # duplicate

# print(emails)

# empty Set
empty_set = set()

# union, intersection, difference
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 | set2) # {1, 2, 3, 4}
# print(set1 & set2) # {2, 3} 
# print(set1 - set2) # {1}



print("\n**************\n")