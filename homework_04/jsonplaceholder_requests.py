"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_json(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            return await response.json()


async def receive_api_data() -> tuple:
    result = await asyncio.gather(
        get_json(url=USERS_DATA_URL), get_json(url=POSTS_DATA_URL)
    )

    return tuple(result)
