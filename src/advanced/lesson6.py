import typing
from functools import wraps

print("**************\n")

# class inheritance

# Base class
class Player:

  def __init__(self, name):
    self.name = name

  # instance method
  def play(self):
    print(F"{self.name} is a player and playing.")

# child class
class Wizard(Player):

  def __init__(self, name, power):
    # call the parent constructor, and pass it's arguments
    super().__init__(name)

    # instance attributes
    self.power = power  

  # override the parent method
  def play(self):
    # call the parent method
    super().play()

    # then add some more logic
    print(F"{self.name} is a wizard and casting a spell.")

wizard1 = Wizard("Merlin", 50)
# print(wizard1.name, wizard1.power) # Merlin 50

# wizard1.play() # Merlin is a wizard and casting a spell.

# multiple inheritance

class Gunner():

  def __init__(self, name, power):
    self.name = name
    self.power = power

  # same name method in both parents -: then python uses MRO
  def play(self):
    print(F"{self.name} is a gunner and shooting a gun.")

class Archer():

  def __init__(self, name, power):
    self.name = name
    self.power = power

  # same name method
  def play(self):

    print(F"{self.name} is an archer and shooting an arrow.")


# multiple inheritance
class Solider(Gunner, Archer):

  def __init__(self, name, power):
    super().__init__(name, power)

soldier = Solider("John", 100)

soldier.play() # John is a gunner and shooting a gun.
# Python uses the MRO (Method Resolution Order) to figure out which parent to use when multiple classes define the same method.

# print(soldier.__class__.__mro__)

# (<class '__main__.Solider'>, <class '__main__.Gunner'>, <class '__main__.Archer'>, <class 'object'>)

is_instance = isinstance(soldier, Gunner) # True
# print(is_instance)
print(issubclass(Solider, Player)) # False

# ====================================
# abstract class

#  inforce methods in child classes

from abc import ABC, abstractmethod

class Character(ABC):
  @abstractmethod
  def attack(self):
    print("attack")

class Hero(Character):
  pass
  # must implement the parent method
  # def attack(self):
  #   print("attack with a sword")

# if Hero does not implement attack() it get an error!
# hero = Hero()
# TypeError: Can't instantiate abstract class Hero without an implementation for abstract method 'attack'

print("\n**************\n")