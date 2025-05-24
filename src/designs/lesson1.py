import typing

print("**************\n")

# design patterns in python

# solid principles

# Single Responsibility Principle (SRP)

# a class should only have one reason to change.
# meaning: one responsibility for a class

class Report:

  def __init__(self, title: str, content: str):
    self.title = title
    self.content = content

  # generate a report
  def generate(self) -> str:
    return f"Title: {self.title}\nContent: {self.content}"

  # also: has the save to file logic here => WRONG!!
  def save_to_file(self, filename: str) -> None:
    print(f"Saving report to {filename}...")

# now the above class has two reasons to change:
  # generate a report
  # save to file

# instead, we can create a separate class for saving the report to a file

class ReportSaver:
  def save_to_file(self, report: Report, filename: str) -> None:
    print(f"Saving report to {filename}...")

#=============================
# Open/Closed Principle (OCP)

# the entity should be open for extension but closed for modification

# ❌ Bad Example:

def calculate_discount(order_type: str, amount: float) -> float:
  match order_type:
    case "regular":
      return amount * 0.1
    case "premium":
      return amount * 0.2
    case "vip":
      return amount * 0.3
    case _:
      raise ValueError("Invalid order type")

# if we want to add a new order type, we have to modify the function

# ✅ Good Example:

from abc import ABC, abstractmethod

# this is like an interface
class DiscountStrategy(ABC):
  # all override apply
  @abstractmethod
  def apply(self, amount: float) -> float:
    pass

class ReqularDiscount(DiscountStrategy):
  def apply(self, amount: float) -> float:
    return amount * 0.1

class PremiumDiscount(DiscountStrategy):
  def apply(self, amount: float) -> float:
    return amount * 0.2

class VIPDiscount(DiscountStrategy):
  def apply(self, amount: float) -> float:
    return amount * 0.3

def calc_discount(order_type: DiscountStrategy, amount: float) -> float:
  return order_type.apply(amount)

discounted = calc_discount(ReqularDiscount(), 100) # 10.0
# print(discounted)

discounted = calc_discount(PremiumDiscount(), 100) # 20.0

# now: we don't change calc_discount!!
# we just add a new class for the new order type
#=============================

# Liskov Substitution Principle (LSP)

# objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program

# for example: if we say Bird can fly, and we have a subclass Penguin, it should not be able to fly
# and this kinda violates the LSP, cause we have a Bird that can not fly so: Penguin is not replaceable with Bird

# ❌ Wrong Example:

"""
class Bird:
  def fly(self) -> str:
    return "I can fly!"

class Penguin(Bird):
  def fly(self) -> str:
    return "I am a Penguin and I can not fly!"
"""

# ✅ Good Example:

class Bird():
  def eat(self) -> str:
    return "I can eat!"

# create a Flyable interface
class Flyable(Bird):
  def fly(self):
    return "I can fly!"

class Penguin(Bird):
  def run(self) -> str:
    return "I am a Penguin and I can run!"

class Sparrow(Flyable):
  def fly(self) -> str:
    return "I am a Sparrow and I can fly!"

# now all Birds can eat
# but only Flyable Birds can fly

birds: typing.List[Bird] = [Sparrow(), Penguin()]

# for bird in birds:
#   print(bird.eat())
  
#   if isinstance(bird, Flyable):
#     print(bird.fly())
#   else:
#     print(bird.run())

# ====================================

# Interface Segregation Principle (ISP)

# a client should not be forced to depend on interfaces it does not use

# WRONG Example:

class Mchine(ABC):
  @abstractmethod
  def print(self) -> None:
    pass

  @abstractmethod
  def scan(self) -> None:
    pass

  @abstractmethod
  def fax(self) -> None:
    pass

class OldPrinter(Mchine):
  def print(self) -> None:
    print("Printing...")

  # forced to implement scan and fax methods even if it does not support them
  def scan(self) -> None:
    raise NotImplementedError("OldPrinter does not support scanning")

  def fax(self) -> None:
    raise NotImplementedError("OldPrinter does not support faxing")

# ✅ Good Example:

# create multiple interfaces

class Printer(ABC):
  @abstractmethod
  def print(self) -> None:
    pass

class Scanner(ABC):
  @abstractmethod
  def scan(self) -> None:
    pass

class Fax(ABC):
  @abstractmethod
  def fax(self) -> None:
    pass

class BasicPrinter(Printer):
  def print(self) -> None:
    print("Printing...")

class FancyPrinter(Printer, Scanner, Fax):
  def print(self) -> None:
    print("Printing...")

  def scan(self) -> None:
    print("Scanning...")

  def fax(self) -> None:
    print("Faxing...")

# ====================================

# Dependency Inversion Principle (DIP)

# high-level modules should not depend on low-level modules. Both should depend on abstractions.

# ❌ Bad Example:

"""
class Database:
  def connect(self) -> None:
    print("Connecting to the database...")

# App depends on Database
class App:
  def __init__(self):
    # App has a dependency on Database
    self.db = Database()
    self.db.connect()
"""

# ✅ Good Example:

class Database(ABC):
  @abstractmethod
  def connect(self) -> None:
    pass

class SQLDatabase(Database):
  def connect(self) -> None:
    print("Connecting to the SQL database...")

class MongoDB(Database):
  def connect(self) -> None:
    print("Connecting to the MongoDB database...")

class App:
  def __init__(self, db: Database) -> None:
    # we pass the dependency to the constructor
    # composition over inheritance
    # dependency injection
    self.db = db
    self.db.connect()

sql_db = SQLDatabase()
mongo_db = MongoDB()

# app = App(sql_db) # pass SQLDatabase
# app = App(mongo_db) # pass MongoDB

"""
# 3 ways for injecting dependencies:

# 1. Constructor Injection
# 2. Setter Injection (property injection)
# 3. Method Injection

"""

print("\n**************\n")