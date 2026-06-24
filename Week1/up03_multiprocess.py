from time import sleep, ctime, time
import multiprocessing

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
    print(f"{ctime()} | === Multi-processing Coffee Machine ===")

    start = time()

    customers = ['A', 'B', 'C']
    processes = []

    for customer in customers:
        process = multiprocessing.Process(target=make_coffee, args=(customer,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end = time()
    print(f"{ctime()} | Total time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
