import copy
# copy values
print("**************\n")

# 🛠️ Lesson 15: Built-in Functions & Standard Library Essentials

# there are functions in python that are built-in to the language, and need no import 

nums = [1, 2, 3, 4]
# print(sum(nums)) # 10

# print(len(nums)) # 4

from datetime import datetime

now = datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

# 2025 5 21 10 45 57

# get the current directory
import os

print(os.getcwd())
# d:\coding\IDEAS\python\syntax

# to json
data = {"username": "alireza", "age": 20, "email": "alireza@alireza"}

import json

# json string
json_str = json.dumps(data)
print(json_str)
print(type(json_str))# str


print("\n**************\n")