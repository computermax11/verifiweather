#!/usr/bin/env python
import sys
from verifiweather import *

def main(args=None):
    if len(sys.argv) > 1 and args == None:
        args = ' '.join(sys.argv[1:])
    print(current_weather(args))

if __name__ == "__main__":
    main()
