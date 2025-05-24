import typing
from abc import ABC, abstractmethod
from typing import List, Any, Dict, Tuple, Iterator
from enum import Enum

print("**************\n")

# this file is all about the open-closed principle

class Color(Enum):
  RED = "Red"
  YELLOW = "Yellow"
  GREEN = "Green"

# item 
class Item:
  def __init__(self, name: str, color: str, price: float = 0.0):
    self.name = name
    self.color = color
    self.price = price

# this is an implementation of the open-closed principle
# so instead of modifying the existing code, we will add new classes.
#  in this case for different types of filters
# we will use the specification pattern to filter the items 

# specification pattern

class Specification(ABC):
  @abstractmethod
  def is_satisfied(self, item: typing.Any) -> bool:
    pass

  # __and__ = and operator
  def __and__(self, other: 'Specification') -> 'Specification':
    # return an instance of AndSpecification
    if not isinstance(other, Specification):
      raise ValueError("Other must be a Specification")
    # pass the current instance and the other instance to AndSpecification  
    print(f"Combining {self.__class__.__name__} with {other.__class__.__name__}")
    return AndSpecification(self, other)

class Filter(ABC):
  @abstractmethod
  def filter(self, items: List[Any], spec: Specification) -> List[Any]:
    pass

# this is for filtering items by color
# but they all have a is_satisfied method
class ColorSpecification(Specification):
  def __init__(self, color: str):
    self.color = color

  # check if the item.color is the same as spec.color
  def is_satisfied(self, item: Any) -> bool:
    return item.color == self.color

# check if the balance is enough to buy the item
class BalanceSpecification(Specification):
  def __init__(self, balance: float):
    self.balance = balance

  def is_satisfied(self, item: Item) -> bool:
    return item.price <= self.balance

# check for two specifications (like color and balance)
class AndSpecification(Specification):
  def __init__(self, spec1: Specification, spec2: Specification):
    # so spec1 = can be color
    self.spec1 = spec1
    # spec2 = can be balance
    self.spec2 = spec2

  def is_satisfied(self, item: Item) -> bool:
    return self.spec1.is_satisfied(item) and \
            self.spec2.is_satisfied(item)

# concrete filter class
class BaseFilter(Filter):
  # a different specification can be passed to the filter method
  def filter(self, items: List[Any], spec: Specification) ->  Iterator[Any]:
    for item in items:
      if spec.is_satisfied(item):
        # yield does not return a list, it returns an iterator
        yield item

items: List[Item] = [
  Item("Apple", Color.RED.value, 1.0),
  Item("Banana", Color.YELLOW.value, 0.5),
  Item("Cherry", Color.RED.value, price=0.8),
  Item("Lemon", Color.YELLOW.value, price=3.5),
  Item("Grapes", Color.GREEN.value, 1.2),
]


# create a filter object
filter = BaseFilter()

"""
# create a color specification for red items
red_spec = ColorSpecification(Color.RED.value)

# filter the items by color
red_items = filter.filter(items, red_spec)

# print the filtered items
for item in red_items:
  print(item.name) # Apple, Cherry
"""

"""
# user balance
BALANCE = 1.0

# filter by balance
balance_spec = BalanceSpecification(BALANCE)

# filter the items by balance
affordable_items = filter.filter(items, balance_spec)

# print the affordable items
for item in affordable_items:
  print(item.name)
"""

# filter by color and balance
red_spec = ColorSpecification(Color.RED.value)
balance_spec = BalanceSpecification(1.0)

# combine the two specifications
# and_spec = AndSpecification(red_spec, balance_spec)

# with __and__ setup =: we can do this
red_affordable_spec = red_spec & balance_spec

# filter the items by color and balance
# red_and_affordable_items = filter.filter(items, and_spec)
red_and_affordable_items = filter.filter(items, red_affordable_spec)

for item in red_and_affordable_items:
  print(f"{item.name} - {item.color} - ${item.price:.2f}")

print("\n**************\n")