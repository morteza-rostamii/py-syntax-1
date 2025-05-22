import typing

print("**************\n")

# 🧠 Intermediate Lesson 26: Iterators & Generators

# iterator 

# any object that returns an iterator is an iterable
# basically: implements: __iter__() and __next__()

numbers = iter([1, 2, 3])

# print(next(numbers)) # 1
# print(next(numbers)) # 2
# print(next(numbers)) # 3

while True:
  try:
    x = next(numbers)
    # print(x)
  # it raises StopIteration
  except StopIteration:
    break

# create a custom iterator class

class Countdown:
  def __init__(self, start):
    # set the initial value. ex: 5
    self.current = start

  def __iter__(self):
    return self
  
  def __next__(self):
    # stop the loop when current is <= 0
    if self.current <= 0:
      raise StopIteration
    
    value = self.current
    # count down
    self.current -= 1
    # return the current value
    return value

# for i in Countdown(5):
#   print(i)# 5, 4, 3, 2, 1

# generator 

# generator is a special type of iterator
# it uses the yield keyword instead of return
# it returns a generator object
# created with function syntax
# yield gives lazy evaluation — memory efficient

# Each yield pauses function execution and resumes from there on next iteration.
def countdown(start):
  while start > 0:
    # get the current value
    yield start
    # count down
    start -= 1

# for i in countdown(4):
#   print(i)

# generator expressions
squares = (x ** 2 for x in range(5))
# you still can call next() on a generator
print(next(squares)) #0
print(next(squares)) #1

print("\n**************\n")