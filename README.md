# forest-fire_detection

## Circuit diagram
 ![circuit diagram](https://github.com/gharishkumar/forest-fire_detection/raw/main/forest_fire_detection_layout_bb.png)
<table class="wikitable">
<tbody><tr>
<th> PIN NO. </th>
<th> SYMBOL </th>
<th> DESCRIPTION
</th></tr>
<tr>
<td> 1, 17 </td>
<td> 3.3V </td>
<td> Power positive (3.3V power input)
</td></tr>
<tr>
<td> 2, 4 </td>
<td> 5V </td>
<td> Power positive (5V power input)
</td></tr>
<tr>
<td> 3, 5, 7, 8, 10, 12, 13, 15, 16 </td>
<td> NC </td>
<td> NC
</td></tr>
<tr>
<td> 6, 9, 14, 20, 25 </td>
<td> GND </td>
<td> Ground
</td></tr>
<tr>
<td> 11 </td>
<td> TP_IRQ </td>
<td> Touch Panel interrupt, low level while the Touch Panel detects touching
</td></tr>
<tr>
<td> 18 </td>
<td> LCD_RS </td>
<td> Command/data register selection
</td></tr>
<tr>
<td> 19 </td>
<td> LCD_SI / TP_SI </td>
<td> LCD display/SPI data input of Touch Panel
</td></tr>
<tr>
<td> 21 </td>
<td> TP_SO </td>
<td> SPI data output of Touch Panel
</td></tr>
<tr>
<td> 22 </td>
<td> RST </td>
<td> Reset
</td></tr>
<tr>
<td> 23 </td>
<td> LCD_SCK / TP_SCK </td>
<td> LCD display/SPI clock of Touch Panel
</td></tr>
<tr>
<td> 24 </td>
<td> LCD_CS </td>
<td> LCD chip selection, low active
</td></tr>
<tr>
<td> 26 </td>
<td> TP_CS </td>
<td> Touch Panel chip selection, low active
</td></tr></tbody></table>


## Modules used
 - [Adafruit_Python_GPIO](https://github.com/adafruit/Adafruit_Python_GPIO)
 - [Adafruit_AMG88xx_python](https://github.com/adafruit/Adafruit_AMG88xx_python)
 - [TFT Display](https://github.com/nopnop2002/Raspberry-ili9325)
 - [Display IC reader](https://github.com/nopnop2002/Raspberry_LCD_ID_Reader)
 - [ili9341](https://github.com/sammyizimmy/ili9341)
 - [blynk-library-python](https://github.com/blynkkk/lib-python)
 - [vshymanskyy_blynk-library-python](https://github.com/vshymanskyy/blynk-library-python)
 - [gpsd,gpsd-clients](https://gpsd.gitlab.io/gpsd/client-howto.html)

## Reference
 - [sensor-output](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor/python-circuitpython)
 - [display](https://www.raspberrypi.org/forums/viewtopic.php?t=257517)
 - [display driver](https://www.waveshare.com/wiki/3.5inch_RPi_LCD_(A))
 - [blynk-python_notify](https://github.com/vshymanskyy/blynk-library-python/blob/master/examples/tweet_notify.py)
 - [gps](https://maker.pro/raspberry-pi/tutorial/how-to-read-gps-data-with-python-on-a-raspberry-pi)
 - [gps robo.in](https://robu.in/interfacing-of-gps-module-with-arduino-and-raspberry-pi/)
