import copy
# copy values
print("**************\n")

# lambda and higher order functions:

# so: functions are objects -> and can be assigned, passed and returned
sum = lambda x, y: x + y
# print(sum(1, 2)) #  3

# map 
elements = [1, 2, 3, 4, 5]
# callback: lambda x: x * x
squared = list(map(lambda x: x * x, elements))

# print(squared)# [1, 4, 9, 16, 25]

# filter
elements = [1, 2, 3, 4, 5]
filtered = list(filter(lambda x: x % 2 == 0, elements))
# print(filtered) # [2, 4]

# return a func from another func
def make_multiplier(n: int) -> callable:
  return lambda x: x * n

# returns a multiply function
multiply_by_3 = make_multiplier(3)

# print(multiply_by_3(3)) # 9

# import modules
import modules.utils as utils

# print(utils.truncate_text("hello world", 10))

from datetime import date
from modules.utils import format_date

# print(format_date(date.today())) # 2025-05-21

import sys
# print(sys.path)




print("\n**************\n")