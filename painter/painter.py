import aggdraw


'''
What should I do?

Hmmmmm

I have 42 units...

What is my goal??

What if I were to create an art piece based off lines based off the units?

Sounds good like a first try.
'''

#dateutc
#tempinf
#tempf
#humidityin
#humidity
#windspeedmph
#windgustmph
#maxdailygust
#winddir
#baromabsin
#baromrelin
#hourlyrainin
#dailyrainin
#weeklyrainin
#monthlyrainin
#yearlyrainin
#solarradiation
#uv
#feelsLike
#dewPoint
#lastRain
#date

# 22 units of data above must be used
def paintarchive()
	weatherarchive = open("weatherarchive.txt")
	
	dateutc = weatherarchive.readline()
	tempinf = weatherarchive.readline()
	humidityin = weatherarchive.readline()
	humidity = weatherarchive.readline()
	windspeedmph = weatherarchive.readline()
	windgustmph = weatherarchive.readline()
	maxdailygust = weatherarchive.readline()
	winddir = weatherarchive.readline()
	baromabsin = weatherarchive.readline()
	baromrelin = weatherarchive.readline()
	hourlyrainin = weatherarchive.readline()
	dailyrainin = weatherarchive.readline()
	weeklyrainin = weatherarchive.readline()
	monthlyrainin = weatherarchive.readline()
	yearlyrainin = weatherarchive.readline()
	solarradiation = weatherarchive.readline()
	uv = weatherarchive.readline()
	feelsLike = weatherarchive.readline()
	dewPoint = weatherarchive.readline()
	lastRain = weatherarchive.readline()
	date = weatherarchive.readline()
	
	d = aggdraw.Draw("RGB",(800,800))
	arc()
