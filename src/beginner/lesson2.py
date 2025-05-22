import copy
# copy values
print("**************\n")

names: list[str] = ["Alice", "Bob", "Charlie"]

# just copy the same reference
names2: list[str] = names

# print(names is names2) # True

# shallow copy

ages = [[1, 2], [3, 4]]

# so: basically outer object is new, but inner objects are the same
shallow_ages = copy.copy(ages)

# shallow_ages[0].append(5)

# print(ages) # [[1, 2, 5], [3, 4]]

# 🧠 A deep copy creates a new object and recursively copies all nested objects — not just the outer shell.

deep_ages = copy.deepcopy(ages)

deep_ages[0].append(6)

# print(ages) # [[1, 2], [3, 4]]

# also: shallow copy
s_ages = ages[:]
# print(s_ages)

# object equality
a = [1, 2]
b = a
c = [1, 2]

# True => cause values are the same
if a == c:
  print("a == c")

# a is not the same object as c
if a is c:
  print("a is c")  
else:
  print("a is not c")

# a is the same object as b (same reference)
if a is b:
  print("a is b")

"""
Use is to compare identities (object references).

Use == to compare values.
"""

print("\n**************\n")