#!/usr/bin/env python
import easygui
import verifiweather

def start_func():
    easygui.msgbox(verifiweather.current_weather())

if __name__ == "__main__":
    if os.name == 'nt':
        start_func()
    else:
        print('This script is only for Windows.  Use verifiweather.py for other OS')

