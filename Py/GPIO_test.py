#Test for the GPIO LED outputs and switch inputs on the Voidnet Viator
import RPi.GPIO as GPIO
import time

LED_FRONT_0 = 6
LED_FRONT_1 = 13
LED_FRONT_2 = 19
LED_FRONT_3 = 26

LED_SIDE_BACK = 23
LED_SIDE_MID = 24
LED_SIDE_FRONT = 25

SW_1 = 21
SW_2 = 20
SW_3 = 16
SW_4 = 12

LEDS_FRONT = [LED_FRONT_0, LED_FRONT_1, LED_FRONT_2, LED_FRONT_3]
LEDS_SIDE = [LED_SIDE_FRONT, LED_SIDE_MID, LED_SIDE_BACK]
LEDS = LEDS_FRONT + LEDS_SIDE
SWITCHES = [SW_1, SW_2, SW_3, SW_4]

GPIO.setmode(GPIO.BCM)

for LED in LEDS:
    GPIO.setup(LED, GPIO.OUT)
    print("LED out set " + str(LED))
    
for SW in SWITCHES:
    GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("SW in set " + str(SW))

switch_dict = dict(zip(SWITCHES, LEDS_FRONT))

for LED in LEDS:
    time.sleep(0.3)
    GPIO.output(LED ,GPIO.HIGH)
    print("LED on " + str(LED))

time.sleep(0.7)

for LED in LEDS:
    time.sleep(0.2)
    GPIO.output(LED, GPIO.LOW)
    print("LED off " + str(LED))
    
while True:
    for SW in SWITCHES:
        GPIO.output(switch_dict[SW],GPIO.input(SW))
        print ("SW " + str(SW) + " is " + str(GPIO.input(SW)))
        

GPIO.cleanup()
