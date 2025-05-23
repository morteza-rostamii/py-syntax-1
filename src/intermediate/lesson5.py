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

# create a custom context manager

class MyContext:
  # runs this first
  def __enter__(self):
    print("Entering the context")
    return self

  # then at the end runs this (clean up)
  def __exit__(self, exc_type, exc_value, traceback):
    print("Exiting the context")
    # if we return True, it suppresses the exception
    return False

with MyContext() as context:
  # after __enter__ runs this
  print("Inside the context", context)
  # raise ValueError("An error occurred") # uncomment to see the exception handling

# 🧠 Intermediate Lesson 39: zip() and enumerate() – Smart Iteration 🔁📦

hats = ["red", "blue", "green"]

# for i, hat in enumerate(hats):
#   print(f"Hat {i}: {hat}")

# zip => combines multiple itrables into a single iterable

class1_names = ["Alice", "Bob", "Charlie"]
class2_names = ["Eve", "Frank", "Grace"]

# loop over both iterables
# for name1, name2 in zip(class1_names, class2_names):
#   print(f"Class 1: {name1}, Class 2: {name2}")

# Class 1: Alice, Class 2: Eve
# Class 1: Bob, Class 2: Frank
# Class 1: Charlie, Class 2: Grace

# unzip
pairs = [('a', 1), ('b', 2), ('c', 3)]
keys, values = zip(*pairs)

# print(keys)
# print(values)
# ('a', 'b', 'c')
# (1, 2, 3)

def show_all(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

# show_all(1, 2, 3, 4, x=10, y=20)
"""
a=1, b=2
args=(3, 4)
kwargs={'x': 10, 'y': 20}
"""

# list comprehension
squares = [x ** 2 for x in range(6)]
# print(squares)  # [0, 1, 4, 9, 16, 25]

# comprehension with if-else
labels = ['even' if x % 2 == 0 else "odd" for x in range(7)]
# print(labels)  # ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even']



print("\n**************\n")