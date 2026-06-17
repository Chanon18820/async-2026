import asyncio
import httpx

async def get_user_name(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['name']
        else:
            return None

async def main():
    name1, name2, = await asyncio.gather(get_user_name(1), get_user_name(2))
    print(f"User 1: {name1}")
    print(f"User 2: {name2}")

if __name__ == "__main__":
    asyncio.run(main())