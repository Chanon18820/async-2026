# Program 1: The First Coroutine Function
# Concept: Understanding async def and how it differs from a normal function.
import asyncio

async def greet():
    print("Hello from the first coroutine function!")

print(type(greet))  # Output: <class 'function'>

