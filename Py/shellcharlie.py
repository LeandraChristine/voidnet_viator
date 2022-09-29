#Utilizing the charlieplexing display from adafruit to show memory usage in a randomized fashion.
#Display updates quicker the more CPU is used on the Pi.

import board
import busio as io
import time
import random
import subprocess

from adafruit_is31fl3731.charlie_wing import CharlieWing as Display

i2c = io.I2C(board.SCL, board.SDA)
display = Display(i2c)

display.fill(0)

while True:
    # Shell scripts for system monitoring from here:
    # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    #cmd = "hostname -I | cut -d' ' -f1"
    #IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = 'cut -f 1 -d " " /proc/loadavg'
    CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
    #cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
    #Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")

    #Extracting the Mem-Usage from the string
    per_pos=MemUsage.find("%")
    MemPercent = int (MemUsage [per_pos-5:per_pos-3])
    MemPercent = max(MemPercent,1)/100

    #blocks are the numbers of LED states potentially changing per loop
    blocks = int(float(CPU))
    
    for i in range(blocks):

        x = random.randrange(0,16)
        y = random.randrange(0,8)

        if random.random() <= MemPercent:
            intensity = random.randrange(0,20)
            display.pixel(x,y,intensity)
        
        else:
            display.pixel(x,y,0)
    
    
    sleepMin = 0.02
    sleepMax = 0.2
    time.sleep(random.uniform(sleepMin,sleepMax))

