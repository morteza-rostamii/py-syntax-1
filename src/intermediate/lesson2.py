import typing

print("**************\n")

# 🧠 Intermediate Lesson 25: Comprehensions (List, Dict, Set, Generator)

# [expression for item in iterable if condition]

#list comprehensions

nums = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in nums]

evens = [num for num in nums if num % 2 == 0]

# print(squares) # [1, 4, 9, 16, 25]
# print(evens) # [2, 4]

# dict comprehensions

squares = {n: n ** 2 for n in range(5)}
# print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# set comprehensions
nums = [1, 2, 3, 4, 5]
# auto removes duplicates
unique_squares = {num ** 2 for num in nums}
# print(unique_squares) # {1, 4, 9, 16, 25}

# generator expressions
gen = (x ** 2 for x in range(10000))
# Useful for large datasets or infinite sequences.
# print(next(gen))# 0 
# print(next(gen))# 1

# nested comprehensions -> loop through a 2d array
matrix =  [[1, 2], [3, 4]]

flattened = [num for row in matrix for num in row]
# print(flattened) # [1, 2, 3, 4]



print("\n**************\n")