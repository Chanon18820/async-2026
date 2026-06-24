from time import sleep, ctime, time
import threading

def update_cup_number(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")

def update_lcd(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

def make_coffee(customer_name):
    update_cup_number(customer_name)
    update_lcd(customer_name)

def main():
    print(f"{ctime()} | === Multi-threading Coffee Machine ===")

    start = time()

    customers = ['A', 'B', 'C']
    threads = []

    for customer in customers:
        thread = threading.Thread(target=make_coffee, args=(customer,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end = time()
    print(f"{ctime()} | Total time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
