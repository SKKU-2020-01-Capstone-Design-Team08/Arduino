import serial
import time as t
import string
import pynmea2
import asyncio
import websockets
import requests
import json

lat = ""
lon = ""
time = ""
date = ""
"""
async def hello():
    uri = "wss://echo.websocket.org"
    async with websockets.connect(uri) as websocket:
        name = gps

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")
"""

# TODO: implement async
def sendData():
    URL = 'http://34.64.124.225/set-location'
    PARAMS ={   
                "wifi_mac":"b8:27:eb:d7:db:38",
                "longitude": str(lon),
                "latitude": str(lat),
                "time":str(date) + " " + str(time)
            }
    HEADERS ={"Content-Type":"application/json"}
    res = requests.get(url=URL,  params = PARAMS)
    
    print(res.url)
    print(res.text)
    #recv = res.json()
    print("> Sent\t\t" + str(time))
    print("< " + str(res))
    print()

while True:
    port="/dev/ttyAMA0"
    ser=serial.Serial(port, baudrate=9600, timeout=0.5)
    if temp == 0:
        newdata=ser.readline()
        temp += 1
        continue   
    newdata=ser.readline().decode()
    #print(newdata)

    if newdata[0:6] == '$GPRMC':
        newmsg=pynmea2.parse(newdata)
        date=newmsg.datestamp
        time=newmsg.timestamp
        lat=newmsg.latitude
        lon=newmsg.longitude
        sendData()
        t.sleep(10)
        #asyncio.get_event_loop().run_until_complete(sendData())

