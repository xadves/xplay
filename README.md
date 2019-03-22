xplay
=====
xplay is a tool for playing Axia Livewire AoIP streams from the command line. Functionally the same as Axia iPlay on Windows, this is a an option for engineers using Linux or OS X. xplay works by piping the audio payload from a multicast RTP stream directly into the SoX utility `play` along with a few stream parameters.

dependencies
=====
You'll need `play` which comes with <a href = "http://sox.sourceforge.net/">SoX</a>, and also `rtpdump` from <a href = "http://www.cs.columbia.edu/irt/software/rtptools/">RTP Tools</a>.

Install on a Raspberry Pi
=====
Install the tools to build from source
```bash
$ sudo apt update
$ sudo apt install -y build-essential
```

Install RTPTools from source
```bash
$ cd ~
$ git clone https://github.com/cu-irt/rtptools.git
$ cd rtptools
$ ./configure
$ make
$ sudo ln -s /home/pi/rtptools/rtpdump /usr/bin/rtpdump
```

Install SoX from Raspbian's repo
```bash
$ sudo apt install -y sox
```

Install xplay from source
```bash
$ cd ~
$ git clone https://github.com/xadves/xplay.git
$ cd xplay
$ sudo chmod +x xplay.py
$ sudo ln -s /home/pi/xplay/xplay.py /usr/bin/xplay
```

Plug your device into your livewire network

Add a route to your livewire network (only required if using more than 1 NIC)
```bash
$ route add -net 239.192.0.0 netmask 255.255.0.0 eth0
```

Create a static address in your livewire network (note: you may have to use a different ip)
```bash
interface eth0
static ip_address=10.110.6.50/24
static routers=
fallback nodhcp
```
restart dhcpcd
```bash
$ sudo service dhcpcd restart
```


Play your livewire channel to test everything worked
```bash
$ xplay 10041
```


setup
=====
If you've installed `play` and `rtpdump` somewhere odd, you'll need to update those paths in xplay.py
```bash
$ chmod +x xplay.py
$ cp xplay.py /usr/local/bin/xplay
```

usage
=====
Make sure you assign your computer an IP address that is on the Axia network. Run xplay with the Axia channel number you'd like to listen in on, and you'll hear the Livewire stream. ^C to end.
```bash
$ xplay 32767
```
