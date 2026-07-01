# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.
import asyncio

async def calculate_bill(customer, base_price):
    await asyncio.sleep(1)  # Simulate a time-consuming calculation
    final_price = base_price * 1.07
    return final_price

async def main():
    task_a = asyncio.create_task(calculate_bill("A", 100))
    task_b = asyncio.create_task(calculate_bill("B", 200))

    result_a = await task_a  # Wait for the task to complete and get the result
    result_b = await task_b  # Wait for the second task to complete and get the result

    print(f"\nFinal Bill A: ${result_a:.2f}")
    print(f"Final Bill B: ${result_b:.2f}")
    print(f"Combined Total Revenue: ${result_a + result_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())