import typing

print("**************\n")

# async and await

import asyncio

# this is a coroutines 
async def say_hello():
  print('say hello start')

  # await 
  await asyncio.sleep(2)

  print('async hello done')

async def say_bye():
  print('say bye start')

  # await 
  await asyncio.sleep(1)

  print('async bye done')

# asyncio.run(say_hello())

# another: coroutine
async def main():
  # await say_hello()
  # await say_bye()

  # in this case, say_hello does not block say_bye
  await asyncio.gather(say_hello(), say_bye())
  
# this blocks the main thread until all async functions are done
# asyncio.run(main())
# this runs at the end of the program
# print("after async is called")

# threading: don't block the main thread! so: we run the event loop in another thread

import threading

# so this function goes to event loop
async def get_data():
  print("go run")

  # mimics the async operation
  await asyncio.sleep(2)

  print("get data done")

# run all async functions in a thread
def run_on_event_loop():
  asyncio.run(get_data())

# run the event loop in another thread
# threading.Thread(target=run_on_event_loop).start()

# print('now, the main thread is not blocked')

print("\n**************\n")