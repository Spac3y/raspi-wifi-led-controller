# raspi-wifi-led-controller
This my approach of controling a led strip using the rPi and Python.
By using the User Datagram Protocol I can send with "netcat" small packages with RGB values to the rPI.
The rPI has a constant open port and changes the led strip to the respective values.

Mentions: 
- Used this repo to create transition between old value and new value:
  https://github.com/thesanjeetc/rgbled 
