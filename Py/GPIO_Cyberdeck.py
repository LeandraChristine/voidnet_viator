import RPi.GPIO as GPIO
import time
import struct
import smbus
import sys

# Global settings
# GPIO is 26 for x728 v2.0 v2.1 v2.2, GPIO is 13 for X728 v1.2/v1.3
#GPIO_PORT 	= 26 right now used by a LED in the wiring...might have to change that...
I2C_ADDR    = 0x36 #address of the power mgt chip in the X728

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


#Function from the SW example on the X728 project page
def readVoltage(bus):

     address = I2C_ADDR
     read = bus.read_word_data(address, 2)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     voltage = swapped * 1.25 /1000/16
     return voltage

#Function from the SW example on the X728 project page
def readCapacity(bus):

     address = I2C_ADDR
     read = bus.read_word_data(address, 4)
     swapped = struct.unpack("<H", struct.pack(">H", read))[0]
     capacity = swapped/256
     return capacity

bus = smbus.SMBus(1) # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

GPIO.setmode(GPIO.BCM)

for LED in LEDS:
    GPIO.setup(LED, GPIO.OUT)
    #print("LED out set " + str(LED))
    
for SW in SWITCHES:
    GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #print("SW in set " + str(SW))

switch_dict = dict(zip(SWITCHES, LEDS_FRONT))

for LED in LEDS:
    time.sleep(0.3)
    GPIO.output(LED ,GPIO.HIGH)
    #print("LED on " + str(LED))

time.sleep(0.7)

for LED in LEDS:
    time.sleep(0.2)
    GPIO.output(LED, GPIO.LOW)
    #print("LED off " + str(LED))
    
while True:
    for SW in SWITCHES:
        GPIO.output(switch_dict[SW],GPIO.input(SW))
        #print ("SW " + str(SW) + " is " + str(GPIO.input(SW)))
        
        #PUT THINGS TO TRIGGER WITH SWITCHES HERE
        
    #Battery charge state display on side LEDs
    capacity = readCapacity(bus)
    #print ("Battery: " + str(capacity))
    if capacity >= 80:
        GPIO.output(LED_SIDE_FRONT,1)
    else:
        GPIO.output(LED_SIDE_FRONT,0)
    if capacity >= 50:
        GPIO.output(LED_SIDE_MID,1)
    else:
        GPIO.output(LED_SIDE_MID,0)
    if capacity>= 20:
        GPIO.output(LED_SIDE_BACK,1)
    else:
        GPIO.output(LED_SIDE_BACK,0)
        
