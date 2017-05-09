# -*- coding: utf-8 -*-
#/usr/bin/python3.6
from datetime import datetime
from neopixel import *
import configparser
import time


# LED strip configuration:
LED_COUNT      = 114            # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.
def clock(strip, color, wait_ms=5000):


        
        color4 = 0
        
        colorFile = configparser.ConfigParser()
        colorFile.sections()
        colorFile.read('color.ini')
        DEFAULT = colorFile['COLOR']
        colorFile = (DEFAULT["ccolor"])
        colorFile = colorFile.split(",")
        color0 = colorFile[0]
        color1 = colorFile[1]
        color2 = colorFile[2]
        color = (Color(int(color0), int(color1), int(color2)))
        print (color)



        
        mi = datetime.now().strftime('%M')
        hour = datetime.now().strftime('%I')
        config = configparser.ConfigParser()
        config.sections()

        config.read('deutsch.ini')
        DEFAULT = config['DEFAULT']
        print ("##########################################")
        print ("Stunde " + hour)
        print ("minute " + mi)

        hourint = int(hour)

        #plus eine stunde
        if int(mi) >= 20 and hourint <= 8:
               
                hour = int(hour) + 1
                x = "0"
                hour = ((x) + str(hour))
                print ("Stunde plus eins gleich kliener 8 " +hour)
       
        if int(mi) >= 20 and hourint >= 9 and hourint <= 11:
               
                hour = int(hour) + 1
                hour = (str(hour))
                print ("Stunde plus eins nach 9 " +hour)
 
        if int(mi) >= 20 and hourint == 12:
               
                hour = ("01")
                print ("Stunde plus eins nach 9 " +hour)

        hour = (DEFAULT[hour])
        h = hour.split(",")
        
                
        for i in range(strip.numPixels()):
                strip.setPixelColor(i, Color(0,0,0))



        #Es ist
        strip.setPixelColor(4, color)
        #strip.setPixelColor(4, (255, 0, 0))
        strip.setPixelColor(5, color)
        strip.setPixelColor(7, color)
        strip.setPixelColor(8, color)
        strip.setPixelColor(9, color)

        # Volle Stunden anzeigen aus ini file
        
        try:
                strip.setPixelColor(int(h[0]), color)
        except:
                print ("")

        try:
                strip.setPixelColor(int(h[1]), color)
        except:
                print ("")
        try:
                strip.setPixelColor(int(h[2]), color)
        except:
                print ("")
        try:
                strip.setPixelColor(int(h[3]), color)
        except:
                print ("")
        try:
                strip.setPixelColor(int(h[4]), color)
        except:
                print ("")
        try:
                strip.setPixelColor(int(h[5]), color)
        except:
                print ("")


        # ab hier beginnt vor
        if int(mi) in range (20,30) or int(mi) in range (45,60):
                fvor = ("vor")
                fvor = (DEFAULT[fvor])
                h = fvor.split(",")


                try:
                        strip.setPixelColor(int(h[0]), color)
                        print ("vor als Wort")
                except:
                        print ("vor no value 1") 
                try:
                        strip.setPixelColor(int(h[1]), color)
                except:
                        print ("vor no value 2")
                try:
                        strip.setPixelColor(int(h[2]), color)
                except:
                        print ("vor no value 3")





        # Ab hier beginnt nach
        if int(mi) in range (35,45) or int(mi) in range (5,15):
                fnach = ("nach")
                fnach = (DEFAULT[fnach])
                h = fnach.split(",")

                try:
                        strip.setPixelColor(int(h[0]), color)
                        print ("nach als Wort")
                except:
                        print ("vor no value 1") 
                try:
                        strip.setPixelColor(int(h[1]), color)
                except:
                        print ("vor no value 2")
                try:
                        strip.setPixelColor(int(h[2]), color)
                except:
                        print ("vor no value 3")
                try:
                        strip.setPixelColor(int(h[3]), color)
                except:
                        print ("vor no value 4") 
        
        # ab hier beginnt halb
        for a in range (20,45):
                halb = ("halb")
                halb = (DEFAULT[halb])
                h = halb.split(",")

                if a == int(mi):
                        
                        try:
                                strip.setPixelColor(int(h[0]), color)
                                print ("halb als Wort")
                        except:
                                print ("halb no value 1") 
                        try:
                                strip.setPixelColor(int(h[1]), color)
                        except:
                                print ("halb no value 2")
                        try:
                                strip.setPixelColor(int(h[2]), color)
                        except:
                                print ("halb no value 3")
                        try:
                                strip.setPixelColor(int(h[3]), color)
                        except:
                                print ("halb no value 4")


        # fuenf minuten als Wort anzeigen
        
        if int(mi) in range (5,10) or int(mi) in range (35,40) or int(mi) in range (25,30) or int(mi) in range (55,60):
                ffuenf = ("fuenf")
                ffuenf = (DEFAULT[ffuenf])
                h = ffuenf.split(",")

                try:
                        strip.setPixelColor(int(h[0]), color)
                        print ("fuenf als Wort")
                except:
                        print ("fuenf als Wort no value 1") 
                try:
                        strip.setPixelColor(int(h[1]), color)
                except:
                        print ("fuenf als Wort no value 2")
                try:
                        strip.setPixelColor(int(h[2]), color)
                except:
                        print ("fuenf als Wort no value 3")
                try:
                        strip.setPixelColor(int(h[3]), color)
                except:
                        print ("fuenf als Wort no value 4") 
                            
                                

        # zehn minuten als Wort anzeigen
        
        if int(mi) in range (10,15) or int(mi) in range (40,45) or int(mi) in range (20,25) or int(mi) in range (50,55):
                fzehn = ("zehn")
                fzehn = (DEFAULT[fzehn])
                h = fzehn.split(",")

                try:
                        strip.setPixelColor(int(h[0]), color)
                        print ("zehn als Wort")
                except:
                        print ("zehn als Wort no value 1") 
                try:
                        strip.setPixelColor(int(h[1]), color)
                except:
                        print ("zehn als Wort no value 2")
                try:
                        strip.setPixelColor(int(h[2]), color)
                except:
                        print ("zehn als Wort no value 3")
                try:
                        strip.setPixelColor(int(h[3]), color)
                except:
                        print ("zehn als Wort no value 4") 
                          



        # viertel als Wort anzeigen
        
        if int(mi) in range (15,20) or int(mi) in range (45,50):
                fviertel = ("viertel")
                fviertel = (DEFAULT[fviertel])
                h = fviertel.split(",")

                try:
                        strip.setPixelColor(int(h[0]), color)
                        print ("viertel als Wort")
                except:
                        print ("fuenf als Wort no value 1") 
                try:
                        strip.setPixelColor(int(h[1]), color)
                except:
                        print ("fuenf als Wort no value 2")
                try:
                        strip.setPixelColor(int(h[2]), color)
                except:
                        print ("fuenf als Wort no value 3")
                try:
                        strip.setPixelColor(int(h[3]), color)
                except:
                        print ("fuenf als Wort no value 4") 



        if (mi[1:] == "1") or (mi[1:] == "6"):
                strip.setPixelColor(0, color)
                
        elif mi[1:] == "2" or (mi[1:] == "7"):
                strip.setPixelColor(0, color)
                strip.setPixelColor(1, color)
                

        elif mi[1:] == "3" or (mi[1:] == "8"):
                strip.setPixelColor(0, color)
                strip.setPixelColor(1, color)
                strip.setPixelColor(2, color)
               

        elif mi[1:] == "4" or (mi[1:] == "9"):
                strip.setPixelColor(0, color)
                strip.setPixelColor(1, color)
                strip.setPixelColor(2, color)
                strip.setPixelColor(3, color)



                #strip.setPixelColor(3, Color(255,255,0))


                

        strip.show()
        time.sleep(wait_ms/1000.0)
	




# Main program:
if __name__ == '__main__':
	
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	strip.begin()

	print ('Press Ctrl-C to quit.')
	while True:
		clock(strip, Color(255, 0, 0))  # rot wipe
