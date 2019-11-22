import asyncio
import csv_generator as csvify
import time
import os

from aiohttp import ClientSession

from aioambient import Client

API_KEY = str(os.environ.get('API_KEY'))
APP_KEY = str(os.environ.get('APP_KEY'))
MAC_ADD = str(os.environ.get('MAC_ADD'))

async def main() -> None:
    """Create the aiohttp session and run the example."""
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
