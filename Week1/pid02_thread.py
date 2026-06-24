from time import sleep, ctime, time
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

    sleep(5)  # จำลองการทำงานของ Thread นี้ 5 วินาที

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] "
          f"[Thread Name: {thread_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

def main():
    queue = ['A', 'B', 'C']

    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] "
          f"[Main TID: {main_tid}] === เริ่มระบบจำลองลูกค้าแบบตู้กาแฟ Multi-Threaded ===")

    start_time = time()

    threads = []

    # สร้าง Thread สำหรับแต่ละลูกค้า
    for customer in queue:
        thread = threading.Thread(target=make_coffee, args=(customer,))
        threads.append(thread)
        thread.start()

    # รอให้ Thread ทั้งหมดเสร็จสิ้น
    for thread in threads:
        thread.join()

    duration = time() - start_time

    print(f"{ctime()} | ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")

if __name__ == "__main__":
    main()