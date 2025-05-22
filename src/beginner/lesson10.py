import copy
import os
import requests
# for async request
import asyncio
import httpx

# copy values
print("**************\n")

# making http request

url: str = 'https://jsonplaceholder.typicode.com/todos'

try:
  # this is a synchronous request (blocking)
  # response = requests.get(url)

  # if response.status_code == 200:
  #   data = response.json()
  #   print(data[0])
  # else:
  #   print(f"Error: {response.status_code}")


  # async request

  async def fetch_data(url: str):
    async with httpx.AsyncClient() as client:
      response = await client.get(url)

      if response.status_code == 200:
        data = response.json()
        print(data[0])
      else:
        print(f"Error: {response.status_code}")

  # run the async function
  # asyncio.run(fetch_data(url))
  # print("Async request completed.")
except Exception as e:
  print(e)

# __name__
# file directly run => __main__
# file is imported as a module => module_name

if __name__ == "__main__":
  print("This file is being run directly.")
else:
  print("This file is being imported as a module.")

print("\n**************\n")