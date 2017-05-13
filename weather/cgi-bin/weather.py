#!/usr/bin/env python
# Verifi Application - Weather App
# https://github.com/computermax11/verifiweather.git

import requests
import json
import os

apikey = "434c503a384eb9244acb0a458a1f5b2c"
baseurl = "http://api.openweathermap.org/data/2.5/weather?"
geourl = "http://freegeoip.net/json/"
ipurl = "http://icanhazip.com/"

# Determine location by IP
if os.environ.has_key('SSH_CLIENT'):
    connectip = os.environ['SSH_CLIENT'].split()[0]
elif os.environ.has_key('REMOTE_ADDR'):
    connectip = os.environ['REMOTE_ADDR']
else:
    connectip = requests.get(ipurl).text.strip()

if connectip:
    locdata = json.loads(requests.get(geourl + connectip).text)
    location = ','.join([locdata['city'], locdata['country_code']])
else:
    location = "Los Angeles,US"

def get_weather(location):
    data = {"q":location, "appid":apikey, "units":"imperial"}
    result = requests.get(baseurl, params=data)
    if result.status_code == 200:
        return json.loads(result.text)
    else:
        raise Exception("API Call Failed")

resultdata = get_weather(location)
outputstring = u"Current weather for {0}: {1}\u00b0 and {2}".format(resultdata['name'], resultdata['main']['temp'],
resultdata['weather'][0]['description'])

if os.environ.has_key("REMOTE_ADDR"):
    print("content-type: text/html\r\n")
    outputstring = outputstring.replace(u'\u00b0', '&#176')
    print(outputstring)
else:
    print(outputstring)


