# Program 9: Dynamically Tracking Tasks in a List
# Concept: Managing multiple generated tasks dynamically by appending them into a standard Python list.
import asyncio
from time import time, ctime

async def serve_customer(name):
    print(f"{ctime()} -> Handling customer {name}")
    await asyncio.sleep(1)  # Simulate serving time
    print(f"{ctime()} -> Done customer {name}!")

async def main():
    start_time = time()
    customers = ["A", "B", "C", "D"]
    tasks_list = []  # List to hold the tasks

    for name in customers:
        t = asyncio.create_task(serve_customer(name))  # Create a task for each customer
        tasks_list.append(t)  # Add the task to the list

    for t  in tasks_list:
        await t  # Wait for each task to complete

    print(f"Served all {len(customers)} customers in {time() - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())