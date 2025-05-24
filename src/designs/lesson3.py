import typing
from abc import ABC, abstractmethod
from typing import List, Any, Dict, Tuple, Iterator
from enum import Enum

print("**************\n")

# LSP Principle (LSP): 
# The Liskov Substitution Principle states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.

# this allows: inheritance and polymorphism

# 👎 Violation Example

"""
class Rectangle:
  def __init__(self, width: float, height: float):
    self.width = width
    self.height = height

  # define a property
  @property
  def width(self) -> float:
    return self._width
  
  @property
  def height(self) -> float:
    return self._height

  @width.setter
  def width(self, value: float):
    self._width = value

  @height.setter
  def height(self, value: float):
    self._height = value

  # area
  def area(self) -> float:
    return self._width * self._height
  
class Square(Rectangle):
  def __init__(self, side: float):
    super().__init__(side, side)

  @Rectangle.width.setter
  def width(self, value: float):
    self._width = self._height = value

  @Rectangle.height.setter
  def height(self, value: float):
    self._width = self._height = value

# a function to print area
def print_area(shape: Rectangle) -> None:
  # set the width and height
  # ☠️🛑 this will cause an error if we pass a Square object
  shape.width = 5
  # here we set the height = 10 and width = 10 =: 10 * 10 = 100
  shape.height = 10

  print(f"Area: {shape.area()}")

ractangle = Rectangle(5, 10)
print_area(ractangle) # prints Area: 50

saure = Square(5)
# ☠️🛑 error cause: square can't have different width and height =: which we assign inside of print_area
print_area(saure)   # prints Area: 100
"""

# ⭐ solution: 

class Shape(ABC):
  @abstractmethod
  def area(self) -> float:
    pass

class Rectangle(Shape):
  def __init__(self, width: float, height: float):
    self.width = width
    self.height = height

  def area(self) -> float:
    return self.width * self.height

class Square(Shape):
  def __init__(self, side: float):
    self.side = side

  def area(self) -> float:
    return self.side * self.side

shapes: List[Shape] = [
  Rectangle(5, 10),
  Square(5),
]

for shape in shapes:
  print(f"Area: {shape.area()}") # prints Area: 50 and Area: 25


print("\n**************\n")