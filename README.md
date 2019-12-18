# Sam

>My take at the Machines in Residence program at Yale Center of Collaborative Arts and Media. Sam is the name of our Ambient Weather machine who sends me data that is presented in visuals, audio, and other mediums. I also call this repository Sam to represent all of the code used to create the data visuals. Feel free to deploy your own Sam using this repo or fork it to create new mediums.

## How to Use It

While the Ambient Weather API helper libraries are in various languages, Sam was created mostly with python 3.7. As of the current state, Sam outputs weather data into a csv file and a txt file. These files would be the basis for data visualizations.

## Dependencies

Sam has been created and tested on a linux machine with Python 3.7. Everything described is from the perspective of this linux machine with Python 3.7. Unless you know what you are doing, I would suggest you to follow these instructions from a Unix based terminal of your own.

Install the following packages:

```
pip install asyncio
pip install aioambient
```

## Execution

Before executing the WeatherAsyncioAPI.py file, you need to get the Application key, API key, and MAC address for your Ambient Weather Machine. You can find it on your [Ambient Weather Dashboard](https://dashboard.ambientweather.net). These are keys that are unique to your weather machine so make sure to keep them secret.

Next, you should clone the repository to your machine using:
```
git clone https://github.com/yale-ccam/sam.git
```

Using the keys you have acquired, you want to set your enter your keys into the const.py.example file.
```
APP_KEY="<<Your APP Key>>"
API_KEY="<<Your API Key>>"
MAC_ADD="<<Your MAC Address>>"
```
After you have set the variables, you can remove the extension .example from the file.


To retrieve the data and write it to weather.txt, launch the following
```
python3 weatherRESTAPI.py
```

## Acknowledgments

* Dana Karwas for enabling me to work with the Machines in Residence program
* Yale's Center for Collaborative Arts and Media for their excellent help 

