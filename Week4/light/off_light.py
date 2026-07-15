# lab_lighting_client.py
import asyncio
from time import ctime, time
import httpx

# --- Config: change these to match your setup ---
BASE_URL = "http://172.16.2.117:8088"   # server address from the dashboard URL
STUDENT_ID = "6710301042"

# All 4 lights, each with its own simulated hardware delay (from the README):
# light_1: 0.5s | light_2: 1.2s | light_3: 2.0s | light_4: 0.8s
LIGHT_IDS = ["light_1", "light_2", "light_3", "light_4"]


async def turn_on_light(client: httpx.AsyncClient, light_id: str):
    """Send a POST request to turn ON a single light.
    This call will block/wait for the light's own hardware delay
    (e.g. light_3 takes ~2.0s to respond) but does NOT block other lights,
    because each call is wrapped in its own asyncio.Task."""
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}"
    response = await client.post(url, json={"status": "ON"})
    data = response.json()
    print(f"{ctime()} | [Light ON] {light_id} -> status: {data.get('current_status')}")
    return data


async def turn_off_light(client: httpx.AsyncClient, light_id: str):
    """Send a POST request to turn OFF a single light.
    Same idea as turn_on_light(), just a different 'status' value."""
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}"
    response = await client.post(url, json={"status": "OFF"})
    data = response.json()
    print(f"{ctime()} | [Light OFF] {light_id} -> status: {data.get('current_status')}")
    return data


async def main():
    async with httpx.AsyncClient(timeout=None) as client:

        print(f"{ctime()} | --- Turning OFF all 4 lights concurrently ---")
        start_off = time()

        off_tasks = [
            asyncio.create_task(turn_off_light(client, light_id))
            for light_id in LIGHT_IDS
        ]
        off_results = await asyncio.gather(*off_tasks)

        elapsed_off = time() - start_off
        print(f"{ctime()} | All {len(off_results)} lights are now OFF.")
        print(f"{ctime()} | Elapsed time (OFF): {elapsed_off:.2f} seconds "
              f"(should be close to the slowest light's delay, ~2.0s).")


if __name__ == "__main__":
    asyncio.run(main())