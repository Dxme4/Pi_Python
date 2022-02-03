import RPi.GPIO as GPIO  #Legge til modulen som gir oss mulighet til å bruke GPIO pins på raspberry pi
import time

GPIO.setmode(GPIO.BCM)

echo = 23
trig = 24
led = 25


GPIO.setup(echo, GPIO.IN) #gjøre echo pin til input
GPIO.setup(trig, GPIO.OUT) #gjøre trig til output
GPIO.setup(led, GPIO.OUT) #gjøre led til output

#Lage main loop
try:
    while True:
        GPIO.output(trig, False)
        time.sleep(0.05)

        GPIO.output(trig, True)
        time.sleep(0.00001) #Det er som delay i arduino
        GPIO.output(trig, False)

        #pulseIn
        while GPIO.input(echo)==0:
            pulseStart = time.time()

        while GPIO.input(echo)==1:
            pulseEnd = time.time()

        duration = pulseEnd - pulseStart

        #measure distance
        distance = duration * 17150

        distance = round(distance, 2)

        print ("Distance: ", distance, "cm")

        if distance < 10: #If distance is 10cm or less, the led will light up
            GPIO.output(led, True)
        else:
            GPIO.output(led, False)
         

# kjøres når vi avslutter programmen
except KeyboardInterrupt:
    print ("setting all GPIO pins to default")
    GPIO.cleanup()
    print ("exiting program")
