#!/usr/bin/python3
from Adafruit_AMG88xx import Adafruit_AMG88xx
import pygame
import os
import math
import time
import serial
import numpy as np
from scipy.interpolate import griddata
from gpiozero import DigitalInputDevice, DigitalOutputDevice
from colour import Color

import BlynkLib
mq_sensor = DigitalInputDevice(22)
sprinkler = DigitalOutputDevice(23)

BLYNK_AUTH = 'QYKFKq67HwiDCzGcs3D3DpHPA3wMBGE9'

# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)


SERIAL_PORT = "/dev/serial0"
gps = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 0.5)

def formatDegreesMinutes(coordinates, digits):
    parts = coordinates.split(".")
    if (len(parts) != 2):
        return coordinates
    if (digits > 3 or digits < 2):
        return coordinates
    left = parts[0]
    right = parts[1]
    degrees = str(left[:digits])
    minutes = str(right[:3])
    return degrees + "." + minutes

#low range of the sensor (this will be blue on the screen)
MINTEMP = 26

#high range of the sensor (this will be red on the screen)
MAXTEMP = 42

#how many color values we can have
COLORDEPTH = 1024

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

#initialize the sensor
sensor = Adafruit_AMG88xx()

points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

#sensor is an 8x8 grid so lets do a square
height = 240
width = 240

#the list of colors we can choose from
blue = Color("indigo")
colors = list(blue.range_to(Color("red"), COLORDEPTH))

#create the array of colors
colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

displayPixelWidth = width / 30
displayPixelHeight = height / 30

lcd = pygame.display.set_mode((width, height))

lcd.fill((255,0,0))

pygame.display.update()
pygame.mouse.set_visible(False)

lcd.fill((0,0,0))
pygame.display.update()

#some utility functions
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#let the sensor initialize
time.sleep(.1)
state = 0
latitude = 0.0
longitude = 0.0
while(1):
    try:
        blynk.run()

        print(sensor.readThermistor())
        if sensor.readThermistor() > 40.0 and mq_sensor.value == 1 and state == 0:
            print("Fire Alert")
            blynk.virtual_write(0, 1, latitude, longitude, "Fire_location")
            blynk.notify("Fire Alert")
            sprinkler.on()
            state = 1
        elif sensor.readThermistor() < 40.0:
            sprinkler.off()
            state = 0
        data = gps.readline()
        data_str = data.decode('ascii')
        message = data[0:6]
        if (message == "$GPRMC"):
            parts = data.split(",")
            if parts[2] == "V":
                print("GPS receiver warning")
            else:
                longitude = float(formatDegreesMinutes(parts[5], 3))
                latitude = float(formatDegreesMinutes(parts[3], 2))
                print("Your position: lon = " + str(longitude) + ", lat = " + str(latitude))
        else:
            pass
        #read the pixels
        pixels = sensor.readPixels()
        pixels = [map(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]

        #perdorm interpolation
        bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')

        #draw everything
        for ix, row in enumerate(bicubic):
            for jx, pixel in enumerate(row):
                pygame.draw.rect(lcd, colors[constrain(int(pixel), 0, COLORDEPTH- 1)], (displayPixelHeight * ix, displayPixelWidth * jx, displayPixelHeight, displayPixelWidth))

        pygame.display.update()
    except Exception as e:
        print(e)
