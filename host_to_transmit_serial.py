import socket
import struct
import serial
import time

looping = True

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while looping:
    try:
        ser = serial.Serial('/dev/ttyACM1', baudrate=9600)
    except:
        print("Board not detected, searching again in 5 seconds...")
        time.sleep(5)
    else:
        print("Board found!")
        looping = False
        
sock.bind(('127.0.0.1', 4444))

while True:         
    data = sock.recv(96)

    if not data: 
        break

    outsim_pack = struct.unpack('I4sH2c7f2I3f16s16si', data)
    
    value = str(round(outsim_pack[6])) + " " + str(round(outsim_pack[5] * 3.6)) + "\n"
    ser.write(bytes(value, encoding='utf8'))
    
sock.close()
