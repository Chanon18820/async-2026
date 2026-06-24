from time import ctime, time
import asyncio
import os
import threading

# ฟังก์ชันจำลองการทำกาแฟแบบ Asynchronous
async def make_coffee(customer_name):
    # ดึง PID และ Thread ID ออกมาดู
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] "
          f"[Thread Name: {thread_name}] กำลังชงกาแฟให้ ลูกค้า {customer_name}...")

    await asyncio.sleep(5)  # จำลองการทำงานของ Coroutine นี้ 5 วินาที

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] "
          f"[Thread Name: {thread_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

async def main():
    queue = ['A', 'B', 'C']

    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"{ctime()} | [Main PID: {main_pid}] "
          f"[Main TID: {main_tid}] === เริ่มระบบจำลองลูกค้าแบบ Asynchronous ===")

    start_time = time()

    # สร้าง Task สำหรับแต่ละลูกค้า
    tasks = [asyncio.create_task(make_coffee(customer)) for customer in queue]

    # รอให้ Task ทั้งหมดเสร็จสิ้น
    await asyncio.gather(*tasks)

    duration = time() - start_time

    print(f"{ctime()} | ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")

if __name__ == "__main__":
    asyncio.run(main())