import typing

print("**************\n")

# Advanced OOP: Metaclasses & Class Creation Magic 🧬

# meta class
class MyMeta(type):

  def __new__(cls, name, bases, attrs):
    print("creating  class", name)
    return super().__new__(cls, name, bases, attrs)

# class with metaclass
class MyClass(metaclass=MyMeta):
  pass

obj1 = MyClass()
# print("obj1", obj1)

# a metaclass that enforces all methods to be lowercase

class LowerCaseMeta(type):
  def __new__(cls, name, bases, attrs):
    for attr in attrs:
      # check if: it is callable and the attribute does not start with __
      if callable(attrs[attr]) and not attr.startswith("__"):
        # check if the attribute is not lowercase
        if attr != attr.lower():
          raise ValueError(f"Method {attr} must be lowercase")

    # pass stuff to the parent class
    # and create the class
    return super().__new__(cls, name, bases, attrs)

# create a class with this metaclass
class MyClass2(metaclass=LowerCaseMeta):
  pass
  # this throws an error
  # def MyMethod(self):
  #   print("MyMethod")

# basically: a metaclass is a class that creates classes
# and it runs before the class is created
# so it can modify the class before it is created

# oop inheritance

class Car:
  def __init__(self, make: str, model:str):
    self.make = make
    self.model = model

  def start(self):
    print("Starting the car")

  def stop(self):
    print("Stopping the car")

# inherit from the Car
class Bus(Car):

  def __init__(self, make: str, model: str, capacity: int):
    # call the parent constructor
    super().__init__(make, model)

    # add the capacity attribute
    self.capacity = capacity

  # override the start method
  def start(self):
    print("Starting the bus")

# create a bus object
bus = Bus("Mercedes", "Sprinter", 20)
# bus.start() # Starting the bus
# bus.stop() # Stopping the car

# composition: has a relationship

class Engine:
  def __init__(self, horsepower: int):
    self.horsepower = horsepower

  def start(self):
    print(F"Starting the engine: {self.horsepower} horsepower")

  def stop(self):
    print(F"Stopping the engine: {self.horsepower}")
  
class Vehicle:
  def __init__(self, make: str, model: str, engine: Engine):
    self.make = make
    self.model = model

    # composition: has a relationship
    self.engine = engine

  def move(self):
    print("Moving the vehicle")
    self.engine.start()

  def stop(self):
    print("Stopping the vehicle")
    self.engine.stop()

# create an car with any engine you want
car = Vehicle("BMW", "X5", Engine(300))
car.move() # Moving the vehicle
car.stop() # Stopping the vehicle

# multiple inheritance

class A:
  def greet(self):
    print("Hello from A")

    # super() -> parent is the first class in the MRO after the current class
    super().greet() # Hello from B

class B:
  def greet(self):
    print("Hello from B")

class C(A, B):
  def __init__(self):
    print("Creating C")
    # super() refers to the first class in the MRO
    super().greet() # Hello from A

c = C()
c.greet() # Hello from A

# this is because of the method resolution order (MRO)

print("MRO:", C.__mro__) # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# this means that the first class in the list is the one that will be used




print("\n**************\n")