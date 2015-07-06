#!/usr/bin/env python
import os, sys, subprocess
def checkRoot():
	if "root" not in os.popen("whoami").read():
		print "plz try 'sudo !!'"
		sys.exit(0)
def checkPaths():
	try:
		os.system("cd /media/usb")
	except:
		os.system("sudo mkdir /media/usb")

def setPathToMusic():
	try:
		path = os.popen("sudo fdisk -l | grep 'sd[b-f][0-9]'").read().split(" ")
		if len(path) == 1:
			print "Can not locate flash drive"
			sys.exit(2)
		else:
			os.system("sudo mount " + path[0] + " /media/usb")
	except:
		print "Something went wrong with the flash drive"
		sys.exit(1)

if __name__ == "__main__":
	checkRoot()
	checkPaths()
	setPathToMusic()
