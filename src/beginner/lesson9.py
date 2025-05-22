import copy
import os
# copy values
print("**************\n")

# reading, write, appending

# open a file
# with is a context manager
# with => handle auto file closing
# r => read mode

try:
  
  # append to a file
  with open("output.txt", 'a') as file:
    file.write("\nNew line")

  # as file =: assigns file object to a variable file
  with open("example.txt", 'r') as file:
    # read file
    content = file.read()
    print(content)

  # read and write
  with open('output.txt', 'r+') as file:
    file.write("\nnew content at the end")

    content = file.read()
    print(content)

  # check if a file exists
  if os.path.exists("output.txt"):
    print("File exists")
  else:
    print("File does not exist")

except Exception as e:
  print(e)



print("\n**************\n")