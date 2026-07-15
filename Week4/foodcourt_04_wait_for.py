# foodcourt_04_wait_for.py
import asyncio
from time import ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301042"
    print(f"{ctime()} | --- [Task 4] Practice using wait_for to handle timeouts ---")

    print(f"{ctime()} | [System] Order sent. Monitoring 2.0s timeout limit...")

    try:
        # Order steak (takes ~4.0s) but enforce a hard 2.0s deadline.
        result = await asyncio.wait_for(
            send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak"),
            timeout=2.0
        )
        print(f"{ctime()} | System Response: {result}")

    except asyncio.TimeoutError:
        print(f"{ctime()} | Timeout occurred: Steak took too long! Leaving the food court now.")

if __name__ == "__main__":
    asyncio.run(main())