# foodcourt_02_gather.py
import asyncio
from time import time, ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301042"
    print(f"{ctime()} | --- [Task 2] Practice using gather to wait for all group orders ---")

    start_time = asyncio.get_event_loop().time()

    task_chicken = asyncio.create_task(
        send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice")
    )
    task_noodle = asyncio.create_task(
        send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles")
    )
    task_steak = asyncio.create_task(
        send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak")
    )

    results = await asyncio.gather(task_chicken, task_noodle, task_steak)

    for result in results:
        print(f"{ctime()} | [Pickup] Shop: {result['shop']} | Menu: {result['menu']} is ready!")

    end_time = asyncio.get_event_loop().time()
    elapsed = end_time - start_time
    print(f"{ctime()} | Total time: {elapsed:.2f} seconds (Equals to the slowest dish).")

if __name__ == "__main__":
    asyncio.run(main())