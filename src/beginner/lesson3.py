import copy
# copy values
print("**************\n")

# python operators and expressions:
# ==

# arithmetic operators:
# +, -, *, /, //, %, **

# floor division: 

# print(3 // 2) # 1

# float division:

# print(3 / 2) # 1.5

# comparison operators:
# ==, !=, >, <, >=, <=

# logical operators:
# and, or, not

# assignment operators:
# =, +=, -=, *=, /=, //=, %=

# identity and membership operators:
# is, is not, in, not in

# i think these are the same object cause: optimization.
obj1: object = "hello"
obj2: object = "hello"

# print(obj1 is obj2) # True

scores: list[int] = [1, 2, 3]
# print(1 in scores) # True
# print(5 not in scores) # True

# is and is not => checks if the objects are the same
# in and not in => checks if the object is in the list 

# control flow: 

# if, elif, else

# ternary expression:
post = {"published": True}
status = "success" if post["published"] else "error"

# print(status) # success

# truthy and falsy values:

# truthy values: (everything that is not falsy)
# True, 1, "hello", [], {}, ()

# falsy values:
# False, 0, "", None, [], {}, (), set(), 0.0

# empty tuple:
x = ()
# print(type(x))

#============================

# loops: 
# for, while

students = ["Alice", "Bob", "Charlie"]

for student in students:
  pass
  # print(student)

i = 0
while i < len(students):
  pass
  # print(students[i])
  i += 1

# also: classic for loop

# for i in range(len(students)):
  # print(students[i])

# break, continue, pass

# range()
# results = range(start=1, stop=5, step=2)

# range() returns a special range object
results = range(1, 6, 2)
# print(list(results))# [1, 3, 5]

# else in a for loop => runs if loop completes without break
# for i in range(3):
#   print(i)
# else:
#   print("Loop finished without break.")

print("\n**************\n")