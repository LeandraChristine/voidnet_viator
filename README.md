# voidnet_viator
Scripts, code and printable 3d-files for the Voidnet Viator Cyberdeck

## Description
A savage, retro-cyberpunk inspired Cyberdeck with a thrilling human interface, finished for the Hackaday Cyberdeck challenge 2022.

The custom made high ergonomic roll-pin mouse pointer allows typing on the mechanical keyboard and mouse movement in the same hand position.
This interface is supported by a wide-screen touchscreen, a psp-knob used for scrolling, stereo speakers, USB Hub, a tiny status OLED, GPIO switches and LEDs, and an
elaborate visualization of the currently used memory.
To enable project building, 5V power is supplied via two banana jacks and a 8 channel signal analyzer mounted under the keyboard.
Highly portable with a grip handle, cable-organizing shoulder strap, a flashlight and two 18650 Lion cells the Viator is a viable companion for your next run.

## BOM

Other than the 3d printed parts the following was used:

### Base
- Raspberry Pi 4 (+SD card)
- Corsair K65 RGB 60% mechanical keyboard (don't get too attached to it)
- Waveshare Raspberry Pi 7.9 inch Capacitive LCD HDMI Display 400 x 1280 (comes with great Raspi HDMI and USB connectors)
- Geekworm Raspberry Pi UPS, X728 V2.1 (or alternative)
- 2x 18650 (unprotected due to the X728 spacing) Lion cells
- 2x Goobay 4-Port USB 2.0 Hub (needs a super slim form factor to fit. I used this: https://www.berrybase.de/4-port-usb-2.0-hub-mit-0-4m-anschlusskabel-farbe-schwarz)
- M3 cylinder screws of various lengths ()
- Wiring (e.g. 0.14mm), Connectors and general soldering stuff
- Threaded inserts / Knurled Nuts (M3)
- (optional) microSD / T-Flash to microSD extension (to get to the SD card easier)

### Rolling mouse
- 8mm stainless steel shaft
- 3x IGUS drylin® R Lineargleitbuchse RJUM-01 (or LM8UU, but it will not feel as nice and smooth)
- optics, chip and bits off a cheap, wired, optical mouse (I used ISY ICM-1000, which has a A2803 optical mouse sensor: http://www.nst-ic.com/nstfileupload/productsinfo/20190703095231_293.pdf)

### Additional Features
- Adafruit 15x7 CharliePlex LED Matrix Display FeatherWing - Red
- Adafruit 2,23 inch OLED for Raspberry Pi Pico, 128x32, SPI/I2C
- AZDelivery Logic Analyzer 8 CH, 24MHz
- 2x 4mm Banana Jacks (22mm length, one red, one black...I did not like the red I got so a 3d file for resin printing your own is included)
- InLine 33441G USB 3.1 Adaptercable Male C to Female C (for the charging port connected to the UPS)
- 0.28" mini Digital Voltmeter Display
- PSP Slim analog Controller Joystick
- Teensy LC (to generate a HID Keyboard and Mouse, you can try a different controller here....but I had some issues with the Circuitpython ones)
- 7x different color 5mm LEDS (and resistors matched to the GPIO output)
- 7x LED housing for 5mm leds (I used Signal Construct 1089)
- 4x Miniature Toggle Switch (I scavenged for these, you can also use any other switches or buttons that fit in the front panel)
- Hefty, vandalism-safe Button with LED indicator for 10mm hole (power button, there is plenty of space reserved for this in the housing so even longer models should fit)
- 5mm hole momentary switch (for below the screen, wired to the waveshare display's on/off switch so it can be used to conserve power)

### Handle
- Bike Handle Grip (Diameter: ~22 mm. Length: ~ 110 mm, cut to size)

### Strap
- 2x Tactical Belt (so you get two buckles to remove the strap completely)
- Some more M3 Bolts & Nuts
- USB or other cables you wish to carry
