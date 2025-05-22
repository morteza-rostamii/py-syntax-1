
print("**************\n")

# variables

username: str = "John Doe"
is_admin: bool = True
age: int = 20
score: float = 3.5

# expression: evaluate to a value
result: int = 2 + 3

# check the type
# print(type(username))

# everything is an object in python

# data types

# primitives: 
  # are immutable
  # int, float, bool, str

# basically: there is no actual primitive in python! everything is an object. a reference to the heap.
number1: int = 2 # 140730670139864
number2: int = number1 # 140730670139864

# print(id(number1))
# print(id(number2))

serial1: str = '1'
serial2: str = '1'

# they are the same object. for optimization: cause they have the same value
# print(id(serial1)) # 140730668234048
# print(id(serial2)) # 140730668234048

# There are no stack-based primitives in Python like in C, C++, or Java.

"""
1. Immutable means: the value on the heap cannot change
When you have an immutable object (like int, float, bool, str, or tuple), it means:

❗ Once created, the internal value of that object cannot be changed.

✅ 2. Assigning a new value creates a new object
Yes! When you reassign a new value to a variable pointing to an immutable object, Python creates a new object on the heap and changes the reference.

If the object is mutable (like a list, dict, set, or a custom class), then the object can be changed in-place without creating a new one.

"""

# ok! so basically in py => the only difference between data types is => some objects are immutable and some are mutable

greeting: str = "hello"

# print(id(greeting)) # 3032289208304

# no if i want to change or reassign a new value here, it will create a new object
greeting += " world"
# print(id(greeting)) # 3032289377328
# print(greeting)

# immutable types
  # int, float, bool, str
  # tuple
  # bytes
  # frozenset

# mutable types
  # list
  # dict
  # set
  # class

# mutable example

my_list: list = [1, 2, 3]
# print(my_list)
# print(id(my_list)) # 2345631683136

my_list.append(4)
# print(my_list)
# print(id(my_list)) # 2345631683136
# so: the list is a reference to the same object

# immutable values => behave like: pass-by-value

def change_value(x: int) -> None:
  # so: x is int => and immutable. so when you try to change it a new value is created => so: outside x is unchanged
  x += 1
  print(x) # 6

# although a reference is passed, the value is not changed
x: int = 5
change_value(x)
print(x) # 5

# now: mutable types => behave like: pass-by-reference

def change_list(lst: list) -> None:
  lst.append(6)
  print(lst) # [1, 2, 3, 4, 5, 6]

numbers: list[int] = [1, 2, 3, 4, 5]
change_list(numbers)
print(numbers) # [1, 2, 3, 4, 5, 6]



print("\n**************\n")