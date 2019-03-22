#!/usr/bin/python
#
# REQUIREMENTS && TESTED
# Tested working with python 2.7.13
# Tested working with rtptools 1.22 (rtpdump)
# Tested working with SoX 14.4.1 (play)
# Tested with Raspberry Pi Running Raspbian 4.14.50-v7
#

#
# Must be on the livewire network
#

import sys
import os
import socket
import struct

RTPDUMP_BIN = "/usr/bin/rtpdump" #change this if your path is different
PLAY_BIN = "/usr/bin/play" #change this if your path is different


def check_bin(bin):
	if os.path.exists(bin) and os.access(bin,os.X_OK):
		return True

def hex2ip(s):
    print struct.pack("<L", s)
    back_ip = socket.inet_ntoa(struct.pack("<L", s))
    split_ip = back_ip.split(".")
    return split_ip[3] + '.' + split_ip[2] + '.' + split_ip[1]+ '.' + split_ip[0]

def main():
	inital_check = True
	if not check_bin(RTPDUMP_BIN):
		print "rtpdump binary could not be found"
		inital_check = False
	if not check_bin(PLAY_BIN):
		print "play binary could not be found"
		inital_check = False
	if len(sys.argv) != 2:
		print "Please supply a valid Livewire channel number (1 - 32767). Correct usage: xplay 32767"
		initial_check = False

	if not inital_check:
		sys.exit(1)


	multicastAddr = int(sys.argv[1]) + 0xEFC00000 #Axia channel number + base IP (239.192.0.0 [in hex])
	#multicastAddr = 0xefc02739 #Axia channel number + base IP (10.110.6.0 [in hex])
        print hex(multicastAddr)
        print hex2ip(multicastAddr)
	os.system(RTPDUMP_BIN + " -F payload " + hex2ip(multicastAddr) + "/5004 | " + PLAY_BIN + " -c 2 -r 48000 -b 24 -e signed-integer  -B -t raw -")


main()
