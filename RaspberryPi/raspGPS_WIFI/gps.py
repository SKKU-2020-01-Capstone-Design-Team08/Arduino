import serial
import time
import string
import pynmea2
import asyncio
import websockets
import requests
import json

temp = 0
gps = ""
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
    URL = "http://34.64.124.225/test"
    data = {"petId":gps}
    headers = {"Content-Type":"application/json"}
    res = requests.post(URL, headers=headers, data=json.dumps(data))
    recv = res.json()
    print("> Sent\t\t" + gps)
    print("< " + recv["msg"])
    print()

while True:
    port="/dev/ttyAMA0"
    ser=serial.Serial(port, baudrate=9600, timeout=0.5)
    if temp == 0:
        newdata=ser.readline()
        temp += 1
        continue   
    newdata=ser.readline().decode()

    if newdata[0:6] == '$GPRMC':
        newmsg=pynmea2.parse(newdata)
        lat=newmsg.latitude
        lng=newmsg.longitude
        gps = "Latitude = " + str(lat) +'\t'+ "Longitude = " + str(lng)
        sendData()
        #asyncio.get_event_loop().run_until_complete(sendData())
