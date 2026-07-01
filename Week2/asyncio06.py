# Program 6: Creating a Concurrent Task
# Concept: Wrapping a coroutine inside asyncio.create_task() to schedule it to run in the background.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer):
    print(f"Starting to cooking from customer {customer}...")
    await asyncio.sleep(1)  # Simulate cooking time
    print(f"Finished cooking for customer {customer}!")

async def main():
    start_time = time()
    task_a = asyncio.create_task(cook_spaghetti("A"))  # Schedule the coroutine to run in the background
    print(f"{ctime()}")

    await task_a  # Wait for the task to complete
    print(f"Total time taken: {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())