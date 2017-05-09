# -*- coding: utf-8 -*-
#/usr/bin/python3.6
from datetime import datetime
#from neopixel import *
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
def clock(wait_ms=50000):
        
        color = configparser.ConfigParser()
        color.sections()
        color.read('color.ini')
        DEFAULT = color['COLOR']
        color = (DEFAULT["ccolor"])
        color = color.split(",")
        print ("Change color = "+ color[0] + ", " + color[1] + ", "+ color[2])


        
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

        print ("Hour INT ")
        print (hourint)

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
        
                



        #Es ist
        try:
                print ("ES ist")
                #strip.setPixelColor(4, color)
                #strip.setPixelColor(5, color)
                #strip.setPixelColor(7, color)
                #strip.setPixelColor(8, color)
                #strip.setPixelColor(9, color)
        except:
                print ("Es ist kann nicht angezeigt werden")
        # Volle Stunden anzeigen aus ini file
        
        try:
                #strip.setPixelColor(int(h[0]), color)
                print (int(h[0]))
        except:
                print ("")

        try:
                print (int(h[1]))
        except:
                print ("")
        try:
                print (int(h[2]))
        except:
                print ("")
        try:
                print (int(h[3]))
        except:
                print ("")
        try:
                print (int(h[4]))
        except:
                print ("")
        try:
                print (int(h[5]))
        except:
                print ("")


        # ab hier beginnt vor
        if int(mi) in range (20,30) or int(mi) in range (45,60):
                fvor = ("vor")
                fvor = (DEFAULT[fvor])
                h = fvor.split(",")


                try:
                        
                        print ("vor als Wort")
                except:
                        print ("vor no value 1") 
                try:
                        print ("vor als Wort")
                except:
                        print ("vor no value 2")
                try:
                        print ("vor als Wort")
                except:
                        print ("vor no value 3")





        # Ab hier beginnt nach
        if int(mi) in range (35,45) or int(mi) in range (5,15):
                fnach = ("nach")
                fnach = (DEFAULT[fnach])
                h = fnach.split(",")

                try:
                        print ("nach als Wort")
                        
                except:
                        print ("vor no value 1") 
                try:
                        print ("nach als Wort")
                except:
                        print ("vor no value 2")
                try:
                        print ("nach als Wort")
                except:
                        print ("vor no value 3")
                try:
                        print ("nach als Wort")
                except:
                        print ("vor no value 4") 
        
        # ab hier beginnt halb
        for a in range (20,45):
                halb = ("halb")
                halb = (DEFAULT[halb])
                h = halb.split(",")

                if a == int(mi):
                        
                        try:
                                
                                print ("halb als Wort")
                        except:
                                print ("halb no value 1") 
                        try:
                                print ("halb als Wort")
                        except:
                                print ("halb no value 2")
                        try:
                                print ("halb als Wort")
                        except:
                                print ("halb no value 3")
                        try:
                                print ("halb als Wort")
                        except:
                                print ("halb no value 4")


        # fuenf minuten als Wort anzeigen
        
        if int(mi) in range (5,10) or int(mi) in range (35,40) or int(mi) in range (25,30) or int(mi) in range (55,60):
                ffuenf = ("fuenf")
                ffuenf = (DEFAULT[ffuenf])
                h = ffuenf.split(",")

                try:
                        
                        print ("fuenf als Wort")
                except:
                        print ("fuenf als Wort no value 1") 
                try:
                        print ("fuenf als Wort")
                except:
                        print ("fuenf als Wort no value 2")
                try:
                        print ("fuenf als Wort")
                except:
                        print ("fuenf als Wort no value 3")
                try:
                        print ("fuenf als Wort")
                except:
                        print ("fuenf als Wort no value 4") 
                            
                                

        # zehn minuten als Wort anzeigen
        
        if int(mi) in range (10,15) or int(mi) in range (40,45) or int(mi) in range (20,25) or int(mi) in range (50,55):
                fzehn = ("zehn")
                fzehn = (DEFAULT[fzehn])
                h = fzehn.split(",")

                try:
                        print ("zehn als Wort")
                except:
                        print ("zehn als Wort no value 1") 
                try:
                        print ("zehn als Wort")
                except:
                        print ("zehn als Wort no value 2")
                try:
                        print ("zehn als Wort")
                except:
                        print ("zehn als Wort no value 3")
                try:
                        print ("zehn als Wort")
                except:
                        print ("zehn als Wort no value 4") 
                          



        # viertel als Wort anzeigen
        
        if int(mi) in range (15,20) or int(mi) in range (45,50):
                fviertel = ("viertel")
                fviertel = (DEFAULT[fviertel])
                h = fviertel.split(",")

                try:
                        print ("viertel als Wort")
                except:
                        print ("viertel als Wort no value 1") 
                try:
                        print ("viertel als Wort")
                except:
                        print ("viertel als Wort no value 2")
                try:
                        print ("viertel als Wort")
                except:
                        print ("viertel als Wort no value 3")
                try:
                        print ("viertel als Wort")
                except:
                        print ("viertel als Wort no value 4") 

                 
        
        if (mi[1:] == "1") or (mi[1:] == "6"):
                print ("1 und 6 min")
                
        elif mi[1:] == "2" or (mi[1:] == "7"):
                print ("2 und 7min")

        elif mi[1:] == "3" or (mi[1:] == "8"):
                print ("3 und 8 min")
               

        elif mi[1:] == "4" or (mi[1:] == "9"):
                print ("4 und 9 min")



                #strip.setPixelColor(3, Color(255,255,0))
        time.sleep(5)




# Main program:
if __name__ == '__main__':
	#strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	#strip.begin()

    print ('Press Ctrl-C to quit.')
    while True:
        clock()

