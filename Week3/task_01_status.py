# Objective: Learn how to query the lifecycle status of a task object.
import asyncio
from time import ctime

async def short_job():
    await asyncio.sleep(1)
    return "Success"

async def main():
    task = asyncio.create_task(short_job())
    
    # ตรวจสอบสถานะทันทีในขณะที่ Task ยังคงทำงานอยู่
    print(f"{ctime()} Is task done? {task.done()}")          # ต้องได้: False
    print(f"{ctime()} Is task canceled? {task.cancelled()}")  # ต้องได้: False
    
    await task # รอให้ Task ทำงานเสร็จสิ้น
    
    # ตรวจสอบสถานะอีกครั้งหลังจาก Task ทำงานเสร็จแล้ว
    print(f"{ctime()} Is task done now? {task.done()}")      # ต้องได้: True
    print(f"{ctime()} Is task canceled now? {task.cancelled()}") # ต้องได้: False

asyncio.run(main())