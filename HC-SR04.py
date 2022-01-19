import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

echo = 24
trig = 23
led = 25

GPIO.setup(echo, GPIO.IN)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)



GPIO.output(trig, False) # HIGH = 1 = GPIO.HIGH = True | LOW = 0 = GPIO.LOW = False
time.sleep(2)

GPIO.output(trig, True)
time.sleep(0.00001)
GPIO.output(trig, False)




#pulseIn
while GPIO.input(echo)==0:
    pulseStart = time.time()
    

while GPIO.input(echo)==1:
    pulseEnd = time.time()
    
    

duration = pulseEnd - pulseStart

#Measure Distance
distance = duration * 17150

distance = round(distance, 2)

print ("Distance: ",distance, "cm")

GPIO.cleanup()