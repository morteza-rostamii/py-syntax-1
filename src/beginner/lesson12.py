import copy
import os
import requests
# for async request
import asyncio
import httpx

# copy values
print("**************\n")

# 🧱 Lesson 20: Object-Oriented Programming (OOP) – Basics

# class: blueprint for creating objects
# object: instance of a class
# attribute: property of an object
# method: behavior of an object

class Animal:
  # constructor
  def __init__(self: object, name: str, species: str) -> None:
    # instance attributes
    self.name: str = name
    self.speed: int = 0
    self.species: str = species

  def make_sound(self: object) -> None:
    print(f"{self.name} makes a sound!")

  def run(self: object) -> None:
    self.speed += 10
    print(F"{self.name} is running at {self.speed} km/h")

# create an instance of the Animal class
animal = Animal("Fido", "dog")
# call the make_sound method on the animal object
animal.make_sound()
animal.run() # Fido is running at 10 km/h

print("\n**************\n")