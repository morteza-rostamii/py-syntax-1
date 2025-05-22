import typing

print("**************\n")

# we can also unpack a tuple or a dict into a function

def greet(username, age):
  print(f"Hello {username}, you are {age} years old.")

# unpack a tuple
args = ("John Doe", 30)
# greet(*args)

# unpack a dict
kwargs = {"username": "John Doe", "age": 30}
# greet(**kwargs)

# nested functions and nonlocal

def outer():

  message = 'Hi'

  def inner():
    # work with the variable from the parent function, as opposed to creating a new local variable
    nonlocal message
    message = 'Hello'
    print(message)

  inner()
  print(message)

# outer() # Hello

# closures: returning functions that remember values from it's outer scope

def multiplier(factor: int) -> callable:
  # inner remembers: factor

  # inner function
  def multiply(n):
    return n * factor
  # return the inner function
  return multiply

# times_three = multiplier(3)
# result = times_three(5)
# print(result) # 15

# ============================

# 🧠 Intermediate Lesson 24: Decorators — Functions That Modify Functions

# decorator pattern

def decorator(func: callable) -> callable:
  def wrapper():
    print("before")
    func()
    print("after")

  return wrapper

def say_my_name():
  print("My name is Alireza")

say_my_name_plus = decorator(say_my_name)

# say_my_name_plus()
# so: basically => decorator is a function that takes a function as an argument and returns a new function. with some extra logic added

# decorator sugar

@decorator
def say_her_name():
  print("her name is Sarah")

# now we just call the same function
# say_her_name()

print("\n**************\n")