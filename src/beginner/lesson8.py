import copy
# copy values
print("**************\n")

# error handling: try, except, finally

"""
try:
  # code that might raise an exception
  num = int(input("Enter a number: "))
  result = 10 / num
  print(result)
except ValueError:
  print("Invalid input. Please enter a number.")
except ZeroDivisionError:
  print("Cannot divide by zero.")

else:
  # code to run if no exceptions occur (success)
  print("No exceptions occurred.")
finally:
  print("This code will always run.")
"""


# raise a custom exception
def divide(a: int, b: int):
  if b == 0:
    # ValueError: value is invalid
    raise ValueError("b cannot be zero.")
  return a / b

try:
  # code that might raise an exception
  divide(10, 0)
except ValueError as e:
  print(e)
finally:
  print("This code will always run.")

# general Exception

try:
  # code that might raise an exception
  divide(10, 0)
except Exception as e:
  print(e)
finally:
  print("This code will always run.")

print("\n**************\n")