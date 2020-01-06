import asyncio
import csv_generator as csvify
import time
from const import API_KEY, APP_KEY, MAC_ADD
from aiohttp import ClientSession
from aioambient import Client

async def main() -> None:

    async with ClientSession() as websession:
        client = Client(
        API_KEY,
        APP_KEY,
        websession)

        data = await client.api.get_device_details(MAC_ADD, end_date="")

        csvify.txt(data, "weather.txt", "w")
        csvify.txtarchive(data, "weatherarchive.txt")

asyncio.get_event_loop().run_until_complete(main())
print('API Completed')
