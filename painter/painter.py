from Pillow import Image, ImageDraw
import aggdraw


'''
So I only have 22 units.

Now I possess a design question. Do I hash all of these units then take 
a portion of the hash? Or do I take a portion of the raw data numbers
instead?

Hash?
Well, if I hash it, it won't really be noticable whether the weather
changes the painting or not. 60 degrees and -10 degrees will be both
just as arbitrary and crazy. Then that means I cannot hash it because
there would be no sense of scale or relation.

Scale?
Now, that brings up the question. Should I set my own
scale? I could force all values to be hexadecimal. From there on, it'd
be a direct translation to color codes.

Of course, that'd make the scale and relation very obvious. Say, 60
degrees converts to a blue and any values between 100 and 0 gives a
blueish tint. This would mean that most warm Spring and Summer days are
blue. That'd be too much blue for me.

Solution?
A solution for that could be simple. I could increase the scale and the
values of the data. Say the range was 1000 - 0. I could increase the 60
degrees with an arbitrary multiplication, such as 60 * ((6+0)*10). This
could increase the data to keep up with the new scale. Since I combine
the digits of the data, there could be a finer degree of change in this
new scale. After the data is multiplied, I could take the hexadecimal
color code. If the hexadecimal becomes too large, I could just remove a
few digits

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
def paintarchive():
	weatherarchive = open("weatherarchive.txt")
	
	dateutc 		= weatherarchive.readline()
	tempinf 		= weatherarchive.readline()
	humidityin 		= weatherarchive.readline()
	humidity 		= weatherarchive.readline()
	windspeedmph	= weatherarchive.readline()
	windgustmph 	= weatherarchive.readline()
	maxdailygust	= weatherarchive.readline()
	winddir 		= weatherarchive.readline()
	baromabsin 		= weatherarchive.readline()
	baromrelin 		= weatherarchive.readline()
	hourlyrainin	= weatherarchive.readline()
	dailyrainin 	= weatherarchive.readline()
	weeklyrainin	= weatherarchive.readline()
	monthlyrainin	= weatherarchive.readline()
	yearlyrainin	= weatherarchive.readline()
	solarradiation	= weatherarchive.readline()
	uv 				= weatherarchive.readline()
	feelsLike 		= weatherarchive.readline()
	dewPoint 		= weatherarchive.readline()
	lastRain 		= weatherarchive.readline()
	date 			= weatherarchive.readline()
	
	d = aggdraw.Draw("RGB",(800,800))
	img = Image.new("RGB",
	arc(tempinf, humidityin, windspeedmph)

paintarchive()
