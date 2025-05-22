import typing

print("**************\n")

# 🧠 Intermediate Lesson 27: Modules & Packages – Organizing Code Like a Pro

nums = [1, 2, 3, 4, 5]

# map returns an iterator
map_result = map(lambda x: x ** 2, nums)
# print(map_result) # <map object at 0x000001D6C5AEC4C0>
# print(map_result.__next__()) # 1
# print(map_result.__next__()) # 4

# convert to a list
squared = list(map_result)
# print(squared) # [1, 4, 9, 16, 25]

# decorator with args

def log_args(func: callable) -> callable:
  # remember -: the wrapper is the function we return =: that calls the original stuff with some extra
  def wrapper(*args, **kwargs):
    # log the arguments
    print(F"arguments were: {args}, {kwargs}")
    # call the function with args
    return func(*args, **kwargs)
  
  # return the decorator wrapper
  return wrapper

@log_args
def add(a: int, b: int) -> int:
  return a + b

# res1 = add(2, 2) # arguments were: (2, 2), {}
# print(res1) # 4

# When you decorate a function, you lose its name and docstring. To preserve them:

from functools import wraps

def my_decorator(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
  return wrapper

@my_decorator
def add(a: int, b: int) -> int:
  return a + b

# res2 = add(2, 2) # arguments were: (2, 2), {}
# print(res2) # 4

# check name and docstring
# print(add.__name__) # add
# print(add.__doc__) # None



print("\n**************\n")