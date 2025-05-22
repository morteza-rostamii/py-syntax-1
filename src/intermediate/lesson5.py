import typing

print("**************\n")

# 🧠 Intermediate Lesson 34: Generators & Iterators – Lazy Evaluation and Infinite Sequences

# infinite counter

def infinite_counter():
  n = 0

  while True:
    # yield kinda pauses the function until the next next() call
    yield n
    n += 1

# we can get infinite sequence, if: used in a loop -: set limit and break
counter = infinite_counter()
# print(next(counter)) # 0
# print(next(counter)) # 1

# 🧠 Intermediate Lesson 35: Context Managers & the with Statement – Managing Resources Gracefully

# A context manager is a tool used to set up and tear down resources automatically, such as opening/closing files, managing database connections, or acquiring/releasing locks.

# with open("data.txt", "r") as file:
#   contents = file.read()

print("\n**************\n")