#!/usr/bin/env python
import sys
from verifiweather import *

def main(args=None):
    if args is None and len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        args = None
    print(current_weather(args))

if __name__ == "__main__":
    main()
