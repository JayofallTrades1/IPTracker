##Traces an IP address using the GeoLiteCity database

import pygeoip
import socket 
import pygeo 
##from geopy.geocoders import Nominatim

gi = pygeoip.GeoIP('GeoLiteCity.dat')

print("IPTracker returns the GeoLocation of the given IP address or URL. Written By Suphasith Usdonvudhikai v1.0 9/10/2017")

userInput = input("Enter 1 for URL; Enter 2 for IP Address Lookup: ")

if userInput == 1:
	userInput = raw_input("Enter Website URL: www.google.com\n")
	IPv4 = socket.gethostbyname(userInput)

elif userInput == 2:
	IPv4 = raw_input("Enter IP address: xxx.xxx.xxx.xxx\n")

else:
	print("Wrong user input")
	quit()

dictionary = gi.record_by_addr(IPv4)
##geolocator = Nominatim()
##lat = dictionary['latitude']
##lon = dictionary['longitude']
##string = "\"" + str(lat) + ", " + str(lon) + "\""
##location = geolocator.reverse("%(lat)s, %(lon)s")
#location = geolocator.reverse("52.509669, 13.376294")
print (dictionary)



