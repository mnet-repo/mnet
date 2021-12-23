#mnet wifi router/repeater depends python3(termux or compatible)

#Find termux from fdroid, then

apt update && apt upgrade && apt install python

#The repeater itself originates from the script found here...

#https://android.stackexchange.com/questions/37141/how-to-use-android-in-wi-fi-repeater-mode-by-bridging-wi-fi-with-access-point

#The captive portal is a fork of this repo...

#https://github.com/nikosft/captive-portal


#Tested on Android 10/11 running OxygenOS and Lineage/AOSP/PHH GSI's

##mrbox23 on XDA
##me.nosaj31@gmail.com
##mnet-repo on Github


#WARNING: EXPIREMENTAL! ROOT REQUIRED! MAY NOT BE SAFE! USE WITH CAUTION
#YOU ARE RESPOSIBLE AFTER ROOTING YOUR DEVICE 


#No cats were harmed while putting this together, or as a result of my own personal use.

#Should be safe, keep it in /data and set permissions as you see fit, if your not sure, I'm not an expert and I've been wrong before. 
#I use /data/bin. 
#Message me, I'll help best I can. This began on a moto e5 play lineageOS(8.1) and finished on moto g7 power lineageOS(9) pay attention for where your devices hostapd.conf lives(start your hotspot). Usually /data/vendor/wifi or /data/misc/wifi use the existing hostapd.conf as skeleton change ssid(2) to $SSID, interface to $AP, hw_mode to $HW, etc.



#Install: 


#Copy mnet/mportal to data ex:

#!/system/bin/sh
mkdir /data/bin
#cp -r $(pwd)/mnet /data/bin/
#chmod 0755 -R /data/bin/mnet
#chown 0.0 -R /data/bin/mnet
#export PATH=/data/bin:$PATH


#Use:

#Start(remove the & to leave in foreground):

#mnet up &

#Stop:

#mnet down

#List connections:

#strings /proc/net/arp

#It's a hackjob at this point.

#Note: The python script will work indepent of mnet script. It can function with android system hotspot or other hotspot/repeater methods. Align the interface/gateway settings in mportal to match. 

##TODO

#This project already works as a repeater, using p2p framework and functions without root.

#https://github.com/Mygod/VPNHotspot

![Included captive portal page(It's click-through. Commented out within mportal is the user/password config it had originally)](https://github.com/mnet-repo/mnet/blob/master/Screenshot_20200216-052137_Firefox_Beta.png)
![Connected confirmation](https://github.com/mnet-repo/mnet/blob/master/Screenshot_20200216-052159_Firefox_Beta.png)
![Example client connection output](https://github.com/mnet-repo/mnet/blob/master/Screenshot_20200216-052250_Terminal_Emulator.png)
![Example output](https://github.com/mnet-repo/mnet/blob/master/Screenshot_20200216-051256_Terminal_Emulator.png)


