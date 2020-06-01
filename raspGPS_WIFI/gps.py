import serial
import time
import string
import pynmea2
import asyncio
import websockets

temp = 0
gps = ""

async def hello():
    uri = "wss://echo.websocket.org"
    async with websockets.connect(uri) as websocket:
        name = gps

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

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
        gps = "Latitude= " + str(lat) + " and Longitude " + str(lng)
        asyncio.get_event_loop().run_until_complete(hello())
