import sys,time,geolocation,publisher
from subprocess import call

SleepTime = 10 # seconds
_lat = 0.00
_lon = 0.00

def maintain():
    global _lat
    global _lon
    x=y
    (lat,lon,accuracy) = geolocation.getLocation()
	
        data = str(lat) + "," + str(lon) + "," + str(accuracy)
        print "publishing ", data
        publisher.publishtoInternet(data)
        _lat = lat
        _lon = lon


       
