# Program 3: The Event Loop (asyncio.run)
# Concept: Using the Event Loop to actually execute a Coroutine Object.
import asyncio

async def greet():
    print("Hello form the Event Loop")

if __name__ == "__main__":
    coro_object = greet()  # Create a coroutine object

    asyncio.run(coro_object)  # This will execute the coroutine and print "Hello"