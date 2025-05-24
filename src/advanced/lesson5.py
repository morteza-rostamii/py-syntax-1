import typing
from functools import wraps

print("**************\n")

class Animal:

  # static attribute
  CLASS_ID: str = "2"

  # constructor
  # color: str=None =: default value (optional argument)
  def __init__(self, name: str, species: str, color: str=None) -> None:
    # instance attributes

    # @private
    # self.name after using @property =: is just an access point for calling the getter or setter
    self.name = name
    self.species = species

    # fully private attribute (2 underscores)
    self.__weight = 0

    # private attribute
    self._color = color or "black"

    # self is the instance object
    # print(f"{self.name} is a {self.species}")

  # instance method
  def make_sound(self) -> None:
    print(f"{self.name} makes a sound!")

  # getter for __weight
  # @property
  # def weight(self) -> int:
  #   return self.__weight

  # we can call the property what ever we want -> what it returns matters
  def get_weight(self) -> int:
    return self.__weight

  # getter
  @property
  def name(self) -> str:
    # self._name is the private attribute now
    return self._name

  # setter
  @name.setter
  def name(self, name: str) -> None:
    self._name = name

  # class method (Static method)
  @classmethod
  def get_class_id(cls) -> str:
    return cls.CLASS_ID

# create an instance of the class
animal = Animal("Fido", "dog")

# call the instance method
# animal.make_sound()

# call the class method
# print(Animal.get_class_id()) # 2
  
# set the animal name
animal.name = "Jane Doe"

# get the animal name
# print(animal.name) # Jane Doe

# access the private variable
dogy = Animal("Husky", "dog", "white")
# _color =: is just a convention
# print(dogy._color) # white

# print(dogy.name)
# print(dogy.__weight)
# Animal' object has no attribute '__weight'
# print(dogy.weight) # 0
# print(dogy.get_weight()) # 0

#===========================================


print("\n**************\n")