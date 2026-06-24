import asyncio
from time import ctime, time

async def update_cup_number(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")

async def update_lcd(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    await asyncio.sleep(1)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

async def make_coffee(customer_name):
    await update_cup_number(customer_name)
    await update_lcd(customer_name)

async def main():
    print(f"{ctime()} | === Asyncio Coffee Machine ===")

    start = time()

    customers = ['A', 'B', 'C']
    tasks = [make_coffee(customer) for customer in customers]

    await asyncio.gather(*tasks)

    end = time()
    print(f"{ctime()} | Total time: {end - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())