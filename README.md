# rpiAssistant
My raspberry pi home assistant project I use in my bedroom for a vertical 7 inch touchscreen of 768x1024.

Uses customtkinter as well as several other libraries such as Adafruit_DHT and gpio-ir.

My home assistant has a DHT11 for checking my room's humidity and temperature, an IR receiver (for registering new remotes) and an IR emitter for sending signals such as controlling my LED strip lights.


# APIs for controlling devices:

python-kasa: https://github.com/python-kasa/python-kasa
PyP100: https://github.com/fishbigger/TapoP100