#!/usr/bin/env python
# https://github.com/computermax11/verifiweather.git

import requests
import os
import sys
import ipaddr

apikey = "434c503a384eb9244acb0a458a1f5b2c"
baseurl = "http://api.openweathermap.org/data/2.5/weather?"
geourl = "http://freegeoip.net/json/"
ipurl = "http://icanhazip.com/"

# Get client IP
def get_client_ip():
    if 'SSH_CLIENT' in os.environ:  # If client is connected by SSH, use the originating IP
        clientip = os.environ['SSH_CLIENT'].split()[0]
        if ipaddr.IPv4Address(clientip).is_private:
            return requests.get(ipurl).text.strip()  # If their IP is private, get the public one
        else:
            return os.environ['SSH_CLIENT'].split()[0]
    elif 'REMOTE_ADDR' in os.environ:   # If being hit from browser, user REMOTE_ADDR environment variable
        return os.environ['REMOTE_ADDR']
    else:
        return requests.get(ipurl).text.strip()  # Get outside IP

# Geolocate by IP
def get_location(ip=get_client_ip()):
    locdata = requests.get(geourl + ip).json()
    if locdata['city'] == '':
        return "Los Angeles,US"
    else:
        return ','.join([locdata['city'], locdata['country_code']])

# Query openweather API
def get_weather(location):
    data = {"q":location, "appid":apikey, "units":"imperial"}
    result = requests.get(baseurl, params=data)
    if result.ok:
        return result.json()
    else:
	print('no weather data for location: %s' % location)
        sys.exit(1)

# Return current weather string
def current_weather(location=None):
    if location == None or location == []:
        location = get_location()
    weatherdata = get_weather(location)
    outputstring = u"Current weather for {0}: {1}\u00b0 and {2}".format(weatherdata['name'], weatherdata['main']['temp'],
weatherdata['weather'][0]['description'])
    if 'REMOTE_ADDR' in os.environ:
        outputstring = "content-type: text/html\r\n" + outputstring.replace(u'\u00b0', '&#176')
    return outputstring

if __name__ == "__main__":
    location = None
    print sys.argv
    if len(sys.argv) > 1:
        location = ' '.join(sys.argv[1:])
    print(current_weather(location))
