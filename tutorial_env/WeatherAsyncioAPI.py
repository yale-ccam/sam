import asyncio
import csv_generator as format
import time
import os

from aiohttp import ClientSession

from aioambient import Client

API_KEY = str(os.environ.get('API_KEY'))
APP_KEY = str(os.environ.get('APP_KEY'))

async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
        client = Client(
        API_KEY,
        APP_KEY,
        websession)

        # Get all devices in an account:
        #await client.api.get_devices()
        data = await client.api.get_device_details('F0:85:C1:E9:C9:00', end_date="")

        format.txt(data, "weather.txt", "w")
        format.txtarchive(data, "weatherarchive.txt")



            #weatherfile.write("1, " + data[])    #dateutc
            #weatherfile.write("2, " + data[])    #date
            #weatherfile.write("3, " + data[])    #winddir
            #weatherfile.write(i + ", " + data[])    #windspeedmph
            #weatherfile.write(i + ", " + data[])    #maxdailygust
            #weatherfile.write(i + ", " + data[])    #windgustdir
            #weatherfile.write(i + ", " + data[])    #winddir_avg2m
            #weatherfile.write(i + ", " + data[])    #windspdmph_avg10m
            #weatherfile.write(i + ", " + data[])    #winddir_avg10m
            #weatherfile.write(i + ", " + data[])    #windspdmph_avg10m
            #weatherfile.write(i + ", " + data[])    #tempf
            #weatherfile.write(i + ", " + data[])    #humidity
            #weatherfile.write(i + ", " + data[])    #baromrelin
            #weatherfile.write(i + ", " + data[])    #baromabsin
            #weatherfile.write(i + ", " + data[])    #tempinf
            #weatherfile.write(i + ", " + data[])    #humidityin
            #weatherfile.write(i + ", " + data[])    #hourlyrainin
            #weatherfile.write(i + ", " + data[])    #dailyrainin
            #weatherfile.write(i + ", " + data[])    #monthlyrainin
            #weatherfile.write(i + ", " + data[])    #yearlyrainin
            #weatherfile.write(i + ", " + data[])    #feelsLike
            #weatherfile.write(i + ", " + data[])    #dewPoint

        # Get all stored readings from a device:
        #await client.api.get_device_details('F0:85:C1:E9:C9:00')

        # A loop at an arbitrary range. Could be changed to a while True.
        #for i in range(1):
            # Get all stored readings from a device (starting at a datetime):
            #data = await client.api.get_device_details('F0:85:C1:E9:C9:00', end_date="") # If end_date is left blank, it shall pull the most recent data
        #csv.generate(data,'w') #modifier can be set to x for new file, a to append to file, and w to overwrite file
            #time.sleep(1)

asyncio.get_event_loop().run_until_complete(main())
print('API Completed')
