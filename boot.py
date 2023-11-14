# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

WIFI_NETWORK_SSID = "Tony_Stark"
WIFI_NETWORK_PASSWORD = "online_async.py"

import network

print("\n[*] Connecting to WiFi Network")
wifi_sta = network.WLAN(network.STA_IF)
wifi_sta.active(True)
wifi_sta.connect(WIFI_NETWORK_SSID, WIFI_NETWORK_PASSWORD)

while not wifi_sta.isconnected():
    print(".", end="")
    time.sleep(0.1)

print("\n[+] Connected to WiFi network with local IP:", wifi_sta.ifconfig()[0])