import asyncio
from http import client
import time
import httpx

# ==========================================
# 1. Configuration & Constants
# ==========================================
STUDENT_ID = "6710301042" 
BASE_URL = "http://172.16.2.117:8088"

# กำหนดลำดับชิ้นส่วนและหุ่นยนต์
PARTS = ["A", "B", "C"]
ROBOTS = ["robot_1", "robot_2", "robot_3", "robot_4"]

# ==========================================
# 2. Async Functions Development
# ==========================================

async def reset_factory(client: httpx.AsyncClient):
    """ส่ง Request เพื่อทำการ Reset สถานะของหุ่นยนต์ทั้งหมดของรหัสนักเรียนนี้"""
    # TODO: เติมโค้ดส่ง POST request ไปยัง /student/{STUDENT_ID}/reset
    url = f"{BASE_URL}/student/{STUDENT_ID}/reset"
    response = await client.post(url)
    data = response.json()
    print(f"Factory reset response: {data}")
    return data

async def grab_part(client: httpx.AsyncClient, robot_id: str, part: str):
    """สั่งให้หุ่นยนต์หยิบชิ้นส่วน 1 ชิ้น"""
    url = f"{BASE_URL}/student/{STUDENT_ID}/robot/{robot_id}/grab"
    payload = {"part": part}
    # TODO: เติมโค้ดส่ง POST request ไปยัง /student/{STUDENT_ID}/robot/{robot_id}/grab
    # พร้อมแนบ JSON Payload {"part": part}
    response = await client.post(url, json=payload)
    data = response.json()
    print(f"Grab part response: {data}")
    return data

async def run_robot_task(client: httpx.AsyncClient, robot_id: str):
    """สั่งให้หุ่นยนต์ 1 ตัว ทำการหยิบชิ้นส่วน A, B, และ C ตามลำดับ"""
    url = f"{BASE_URL}/student/{STUDENT_ID}/robot/{robot_id}/grab"
    # TODO: วนลูปหยิบชิ้นส่วนใน PARTS ตามลำดับเรียงกัน (Sequential inside single robot)
    for part in PARTS:
        await grab_part(client, robot_id, part)
    

async def main():
    """Main function to run the robot tasks."""
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=10.0) as client:
        print("Resetting Factory...")
        await reset_factory(client)

        
        start_time = time.time()
        results = []
        for i in range(len(ROBOTS)):
            robot_id = ROBOTS[i]
            result = await run_robot_task(client, robot_id)
            results.append(result)
        print("Starting Async Robot Operation...")

        
        elapsed_time = time.time() - start_time
        print(f"Finished all tasks in {elapsed_time:.2f} seconds.")


    #ผมทำให้มันติดสี่ตัวพร้อมกันไม่เป็นครับผมขอโทษครับ
        

if __name__ == "__main__":
    asyncio.run(main())