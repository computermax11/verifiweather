# verifiweather #

## DevOps Engineer Job Application ##

* Find out the current weather for Los Angeles
* Print your result
* Expand upon the script as much as you wish to show us your creativity
* Upload your project to github, and provide directions for setting up and executing your script.

---
## Install #
The program can be installed using python setuptools.
```python setup.py install```

## Use ##
```verifiweather <location>```

The program can be run either from the command line or as a cgi script.  If a location is not given, the script will
try to determine your location by IP (of SSH connection, outbound IP, or of web visitor).  
The current weather will then be displayed.  To view the weather in a browser, use the included runcgi.sh shell script for linux.

### Compatibility ###
The script will run on Python 2.7 as well as Python 3 (tested 3.5).  It also works on both Linux and Windows
