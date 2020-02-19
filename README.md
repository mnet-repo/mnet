#mnet wifi repeater with python2.7(py4a mod)

#My other account(working on recovering access, currently locked out) has the early versions.

#The repeater itself originates from the script found here...

#https://android.stackexchange.com/questions/37141/how-to-use-android-in-wi-fi-repeater-mode-by-bridging-wi-fi-with-access-point

#The captive portal is a fork of this repo...

#https://github.com/nikosft/captive-portal


#Tested on Android 8.1 and 9 running Lineage/AOSP based roms.

##mrbox23 on XDA
##me.nosaj31@gmail.com
##mnet-repo on Github


#WARNING: EXPIREMENTAL! ROOT REQUIRED! MAY NOT BE SAFE! USE WITH CAUTION
#YOU ARE RESPOSIBLE AFTER ROOTING YOUR DEVICE AND PLAYING WITH STUFF LIKE THIS!


#No cats were harmed while putting this together, or as a result of my own personal use.


#Should be safe, keep it in /data/local and set permissions as you see fit, if your not sure, I'm not an expert and I've been wrong before. 
#I use /vendor/usr/bin personally for persistence across rom flashing. 
#Message me, I'll help best I can. This began on a moto e5 play lineageOS(8.1) and finished on moto g7 power lineageOS(9) pay attention for where your devices hostapd.conf lives(start your hotspot). Usually /data/vendor/wifi or /data/misc/wifi use the existing hostapd.conf as skeleton change ssid(2) to $SSID, interface to $AP, hw_mode to $HW, etc. 
#Check example configs.  Works on both Oreo and Pie for me with slight variations between. This uses /data/vendor/wifi if your running oreo, change the DIR variable at the beginning of mndt script.


#Install: 


#Copy mnet_python_standalone dir to data ex:

#!/system/bin/sh

#cp -r $(pwd)/mnet_python_standalone /data/local/mnet
#chmod 0755 -R /data/local/mnet
#chown 0.0 -R /data/local/mnet
#export $PATH:/data/local/mnet/bin


#Use:

#Start(remove the & to leave in foreground):

#mnet up &

#Stop:

#mnet down

#List connections:

#mnet arp

#It's a hackjob at this point. Hopefully smarter people pitch in ;)

#Note: The mportal python script, Along with the self contained python2.7 directory will work indepent of mnet script. It can function with android system hotspot or other hotspot/repeater methods. Align the interface/gateway settings in mportal to match. 

##TODO

#Harden portal method

#Learn python more, slim installation size

#Add options to customise/add portal html/php/auth easier  easier

#Add ability source/modify existing hostapd configuration and pull info from device environment.

#Write interactive menu for launching and configuration

#Study other github projects for ideas and working code for example.. 

#Interactive menu and servers for portal...
  
#https://github.com/rajkumardusad/MyServer

#This project already works as a repeater, using p2p framework and functions without root.

#https://github.com/Mygod/VPNHotspot

![Included captive portal page(It's click-through. Commented out within mportal is the user/password config it had originally)](https://github.com/mnet-repo/mnet/blob/master/Screenshot_20200216-052137_Firefox_Beta.png)
![Connected confirmation](https://github.com/mnet-repo/mnet/blob/master/Screenshot_20200216-052159_Firefox_Beta.png)
![Example client connection output](https://github.com/mnet-repo/mnet/blob/master/Screenshot_20200216-052250_Terminal_Emulator.png)
![Example output](https://github.com/mnet-repo/mnet/blob/master/Screenshot_20200216-051256_Terminal_Emulator.png)


