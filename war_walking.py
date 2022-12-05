#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time
import androidhelper as android 

droid = android.Android()

def updateGpsLocation():
    droid.startLocating()
    
    # sleep during location update
    time.sleep(5)
    
    droid.stopLocating()

    location = droid.getLastKnownLocation().result
    return location.get('gps')

def print_gps_info(gps):
    print()
    print("altitude: "+str(gps['altitude']))
    print("latitude: "+str(gps['latitude']))
    print("longitude: "+str(gps['longitude']))
    print("speed: "+str(gps['speed']))
    print("accuracy: "+str(gps['accuracy']))   
    print()

def print_network_info(network):
    print("ssid: "+ network['ssid'])
    print("bssid: "+network['bssid'])
    print("level:"+str(network['level']))
    print("security: "+network['capabilities'])
    print('\n\n')


while True:    
    # Sleep for a sec
    gps = updateGpsLocation()
    print_gps_info()
    
    time.sleep(3)
    
    networks = droid.wifiGetScanResults()[1]

    while open('/storage/emulated/0/Documents/war_walking_loot.txt', 'w+') as loot:
        loot.writeline(str(gps['altitude']))
        loot.writeline(str(gps['latitude']))
        loot.writeline(str(gps['longitude']))
        loot.writeline(str(gps['speed']))
        loot.writeline(str(gps['accuracy']))
        loot.writeline()

        for idx, network in enumerate(networks):
            if network['ssid'] is not None and network['ssid'] != "" and network['ssid'] != " ":
                print_network_info(network)

                loot.writeline(network['ssid'])
                loot.writeline(network['bssid'])
                loot.writeline(network['level'])
                loot.writeline(network['capabilities'])
                loot.writeline()
                loot.writeline('-----------------------------------------------------')
                loot.writeline('-----------------------------------------------------')
