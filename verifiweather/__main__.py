#!/usr/bin/env python
import sys
from verifiweather import *

def main(args=None):
    print(current_weather())
#    if args is None:
#        args = sys.argv[1:]
#    print(current_weather(args))

if __name__ == "__main__":
    main()