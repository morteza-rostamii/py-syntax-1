import typing
from functools import wraps

print("**************\n")

# pass arguments to decorator

# this take the argument to decorator
def repeat(n: int) -> callable:
  # this is the decorator
  def decorator(func: callable) -> callable:
    # this is the wrapper to decorate and add the extra stuff
    def wrapper(*args, **kwargs):
      # do some extra
      print("some thing extra before")

      # run the decorated function with args
      for _ in range(n):
        func(*args, **kwargs)

    # return the wrapper
    return wrapper

  # return the decorator
  return decorator

# use decorator with args
@repeat(3)
def send_love(name: str) -> None:
  print(F"Sending love to {name}")

# send_love("John Doe")
"""
some thing extra before
Sending love to John Doe
Sending love to John Doe
Sending love to John Doe
"""

# a class decorator

def add_repr(cls: typing.Type) -> typing.Type:
  # add a cusome repr to the class 
  def __repr__(self) -> str:
    # cls is the class
    return f"<{cls.__name__} instance>"

  # add the repr function (from above) to the class
  cls.__repr__ = __repr__

  # return the class 
  return cls

@add_repr
class Dog:
  pass

# object
dog = Dog()
# print(dog) # <Dog instance>

# decorate a class method
def log_method(func: callable) -> callable:
  # this is for: maintain the name and docstring
  @wraps(func)
  def wrapper(self, *args, **kwargs): 
    # print the function name
    print(f"{func.__name__} was called.")

    # call the original function and return the result
    return func(self, *args, **kwargs)

  # return the wrapper
  return wrapper

class Person:
  @log_method
  def jump(self, height: int) -> None:
    print(F"Jumping {height} cm high")

person = Person()
person.jump(100) # Jumping 100 cm high


print("\n**************\n")