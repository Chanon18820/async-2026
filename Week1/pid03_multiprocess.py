from time import sleep, ctime, time
import multiprocessing
import threading
import os

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    # ดึง PID และ Thread ID ออกมาดู
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] "
          f"[Thread Name: {thread_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}...")

    sleep(5)  # จำลองการทำงานของ Process นี้ 5 วินาที

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] "
          f"[Thread Name: {thread_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

def main():
    queue = ['A', 'B', 'C']

    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] "
          f"[Main TID: {main_tid}] === เริ่มระบบจำลองลูกค้าแบบ Multi-Process ===")

    start_time = time()

    processes = []

    # สร้าง Process สำหรับแต่ละลูกค้า
    for customer in queue:
        process = multiprocessing.Process(target=make_coffee, args=(customer,))
        processes.append(process)
        process.start()

    # รอให้ Process ทั้งหมดเสร็จสิ้น
    for process in processes:
        process.join()

    duration = time() - start_time

    print(f"{ctime()} | ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")

if __name__ == "__main__":
    main()
    