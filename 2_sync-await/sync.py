import asyncio

async def get_num(num: int):
    return num

async def main():
    n = await get_num(2)
    print(n)

asyncio.run(main())
