import copy
# copy values
print("**************\n")

# functions:

# default params
def add(a: int = 0, b: int = 0) -> int:
  return a + b

# print(add()) # 0
# print(add(1)) # 1
# print(add(1, 2)) # 3

# keyword arguments
# print(add(a=1, b=2)) # 3

# arbitrary number of arguments

def add_all(*args: int) -> int:
  # tuple
  print(type(args))

  total = 0
  for num in args:
    total += num
  return total

# add_all(1, 2, 3, 4, 5)

# arbitrary number of keyword arguments

def add_all2(**kwargs: int) -> int:
  # dict
  print(type(kwargs))

  total = 0
  for num in kwargs.values():
    total += num
  return total

# return value and scope:

# multiple return values

def get_info() -> tuple[str, int]:
  name = "John Doe"
  age = 20  
  return name, age

# so: it returns a tuple with all the values
# print(get_info())# ('John Doe', 20)

# scope

# global scope

# global variable
name = "John Doe"
age = 12

# local scope
def greet():
  # python can find a local name -> but: i am accessing it before it is defined
  # print("-", name) ❌ error. reason: 

  # access the global name like this
  # global name
  # after global => you can also change the value
  # name = "Alice Doe"
  # print("global name: ", name)

  # access the global variable
  print(age) # 12

  # local variable => inside the scope of a function
  # also: can't change the global from function => unless global keyword used
  name = "Jane Doe"
  print(f"local name: {name}") # Hello Jane Doe

print(greet())

# if: global is used inside the function -> the global variable can be reassigned instead of creating a local
print("print from global scope: ", name) # John Doe



print("\n**************\n")