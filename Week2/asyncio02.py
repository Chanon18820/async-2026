# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.
import asyncio

async def greet():
    print("Hello")
    
# Calling the async function does not execute it, it returns a coroutine object
coro_object = greet()

# Notice that the coroutine object is created but not executed yet
print(type(coro_object))  # Output: <class 'coroutine'>

# To prevent the program from exiting before the coroutine is executed, we can run it using asyncio.run()
# We will learn more about this in the next program.
coro_object.close()  # Close the coroutine object to clean up resources