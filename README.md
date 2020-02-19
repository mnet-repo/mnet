#mnet wifi repeater with python2.7(py4a mod)

This project originates from a script I found here...
 
https://android.stackexchange.com/questions/37141/how-to-use-android-in-wi-fi-repeater-mode-by-bridging-wi-fi-with-access-point  

The captive portal was modified from this repo...



Tested on Android 8.1 and 9 running Lineage/AOSP based roms.

My other Github acct has the early versions. I'm currently locked out of it.

##mrbox23 on XDA
##me.nosaj31@gmail.com
##mnet-repo on Github


#WARNING: EXPIREMENTAL! ROOT REQUIRED! MAY NOT BE SAFE! USE WITH CAUTION
#YOU ARE RESPOSIBLE AFTER ROOTING YOUR DEVICE AND PLAYING WITH SHIT LIKE THIS!


#No cats were harmed while putting this together, or as a result of my own personal use.


#Should be safe, keep it in /data/local if your not sure. I use /vendor/usr/bin personally for persistence. Message me, I'll help best I can. This began on a moto e5 play lineageOS(8.1) and finished on moto g7 power lineageOS(9) pay attention for where your devices hostapd.conf shows up(start your hotspot). Usually /data/vendor/wifi or /data/misc/wifi use the existing hostapd.conf as an example, this will be device specific. Works on both Oreo and Pie for me with slight variations between. This uses /data/vendor/wifi if hour running oreo change this at the biginning of script.





#Install: 


#Copy mnet_python_standalone dir to data ex:

#!/system/bin/sh

cp -r $(pwd)/mnet_python_standalone /data/local/mnet
chmod 0755 -R /data/local/mnet
chown 0.0 -R /data/local/mnet
export $PATH:/data/local/mnet/bin


#Use:

Start repeater(connect to wifi first)

mnet up &

Stop repeater

mnet down

List connected devices

mnet arp

List usage 

mnet

