import RPi.GPIO as GPIO 
import time 
import LCD_I2C

 

GPIO.setmode(GPIO.BCM) 	# alternative GPIO .board 

 

signal = 21 

 

GPIO.setup(signal, GPIO.IN)  

try: # stoppe programmet. Det gir muligheten til aa bruke med ctr C 
    while 1: 
        val = GPIO.input(signal)  # read FC-51 out pin 
        print(val) 

        time.sleep(0.5) 

except KeyboardInterrupt:  # stop program med ctrl c 
               print ("setting all GPIO pins to default")# 
               GPIO.cleanup()	#set all GPIO to default state 
               print ("exiting program") 