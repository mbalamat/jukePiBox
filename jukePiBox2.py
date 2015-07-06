#!/usr/bin/env python
import os, sys, subprocess

def jukebox():
        try:
                subprocess.call("xmms2 clear")
                subprocess.call("xmms2 add /media/usb/music/*.mp3")
                subprocess.call("xmms2 playlist shuffle")
                subprocess.call("xmms2 play")
        except:
                print "Please check if you have xmms2 installed and try again"

if __name__ == "__main__":
	jukebox()
