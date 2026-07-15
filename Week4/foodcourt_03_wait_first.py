# foodcourt_03_wait_first.py
import asyncio
from time import ctime, time
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301042"
    print(f"{ctime()} | --- [Task 3] Practice using wait (FIRST_COMPLETED) ---")

    start_time = time()

    t1 = asyncio.create_task(
        send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Thigh"))
    t2 = asyncio.create_task(
        send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Wonton Noodles"))
    t3 = asyncio.create_task(
        send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak"))

    # Wait until the FIRST task finishes; the rest stay in 'pending'.
    done, pending = await asyncio.wait(
        {t1, t2, t3},
        return_when=asyncio.FIRST_COMPLETED
    )

    # There's only 1 task in 'done' since we stopped at FIRST_COMPLETED.
    for finished_task in done:
        result = finished_task.result()
        print(f"{ctime()} | Winner served dish: Shop: {result['shop']} | Menu: {result['menu']}")

    # Cancel whatever is still pending to avoid wasting resources.
    print(f"{ctime()} | Cleaning up: Canceling {len(pending)} remaining pending orders...")
    for p in pending:
        p.cancel()

    total_time = time() - start_time
    print(f"{ctime()} | Total waiting time for the first dish: {total_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())