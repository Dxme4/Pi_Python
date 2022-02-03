import RPi.GPIO as GPIO
import time

sensor = 21
buzzer = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print ("IR Sensor Klar.....")
print (" ")

try:
    while True:    #True = 1
        if GPIO.input(sensor)==0:
            GPIO.output(buzzer,True)
            print("Objekt Oppdaget")
            time.sleep(0.5)
        else:
                GPIO.output(buzzer,False)
                print("Ingen hindring!!")
                time.sleep(0.5)
except KeyboardInterrupt:
    print ("setting all GPIO pins to default") 
    GPIO.cleanup()  #set all GPIO to default state
    print("exiting program")