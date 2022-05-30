    # 19 red 13 blue 12 green

# import os
import RPi.GPIO as GPIO
import socket
from rgbled import rgbled
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

udp_ip_listen = "200.200.13.13"
udp_port_listen = 8125

sock =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip_listen, udp_port_listen))

r_pin = 14
g_pin = 15 
b_pin = 18

led = rgbled(r_pin,b_pin,g_pin)

r1 = 0
g1 = 0
b1 = 0

while True:
    try:
        data = sock.recv(udp_port_listen)
        # print(data.decode().split())
        
        r2 = int(data.decode().split()[0])  
        g2 = int(data.decode().split()[1]) 
        b2 = int(data.decode().split()[2])
        print(r2,g2,b2)
                
        r_new = int((r2*100)/255)
        g_new = int((g2*100)/255)
        b_new = int((b2*100)/255)

        led.changeto(r_new,b_new,g_new,1)

        r1 = r2
        g1 = g2 
        b1 = b2

    except KeyboardInterrupt:
        led.off(1)
        led.cleanup()
        exit()
    except RuntimeError:
        time.sleep(2)

 
