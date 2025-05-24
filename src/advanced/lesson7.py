import typing
from functools import wraps
from abc import ABC, abstractmethod

print("**************\n")

# Encapsulation

"""
Modifier	  Syntax	    Access Level
Public	    self.name	  Accessible everywhere
Protected	  _self.name	Internal use / subclasses
Private	    __self.name	Class-private (name-mangled)
"""

# abstraction

"""
🎯 Why Use Abstraction?
To enforce consistent APIs across different classes

To reduce complexity and increase code readability

To follow the "program to an interface" principle

To define what a class must do, not how

"""

class SpaceShip(ABC):
  @abstractmethod
  def launch(self):
    pass
  
class Falcon9(SpaceShip):
  # must implement the abstract method
  def launch(self):
    print("Falcon 9 is launching...")

class FalconHeavy(SpaceShip):
  def launch(self):
    print("Falcon Heavy is launching...")

# now all type SpaceShip can launch
spaceships: typing.List[SpaceShip] = [Falcon9(), FalconHeavy()]

# this is also: polymorphism -> any type of SpaceShip can launch
# for spaceship in spaceships:
#   spaceship.launch()

"""
🔏 Abstraction is about enforcing a contract:
You create an abstract class to define common behavior that all child classes must follow.

The abstract class contains abstract methods — just method signatures, not actual implementations.

Every subclass must implement these abstract methods — otherwise, they can’t be instantiated.
"""

"""
🔥 Real-World Analogy
You press a button labeled Start on different machines:

On a Car, it starts the engine.

On a Coffee Machine, it brews coffee.

On a Computer, it boots up.

You don’t care how it works — you just know all machines can be start()ed.

That’s polymorphism. ✨
"""

# python does not have method overloading like this: 
"""
# basically: same_method name but different parameters : it is not a thing in python

class Something:

  def some_method(self, arg: str):

  # so: the last method will be used
  def some_method(self, arg: int):

"""

print("\n**************\n")