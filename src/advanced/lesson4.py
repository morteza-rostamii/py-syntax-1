import typing
from functools import wraps

print("**************\n")

# set a meta class for Weapon
class WeaponMeta(type):
  def __new__(cls, name, bases, attrs, **kwargs):
    attrs["name"] = name
    return super().__new__(cls, name, bases, attrs)

class Weapon(metaclass=WeaponMeta):

  def __init__(self, name: str, damage: int) -> None:
    self.name = name
    self.damage = damage

  def __repr__(self) -> str:
    return f"<{self.name} instance>"

# print(type(Weapon)) # <class 'type'>
# after setting the metaClass
# print(type(Weapon)) # <class '__main__.WeaponMeta'>

# so a meta class is a class that is used to create other classes

import inspect

class User:
  def __init__(self, name: str, age: int) -> None:
    self.name = name
    self.age = age

user = User("John Doe", 20)

try: 
  pass
  # this just prints the source code of the class
  # print(inspect.getsource(User))
  # print(inspect.getsource(user))

except Exception as e:
  print(e) 

# this syntax unpacks everything between i1 and i3 into a list
my_tuple = (1, 2, 3, 4)

i1, *i2, i3 = my_tuple

# print(i1, i2, i3) # 1 [2, 3] 4




print("\n**************\n")