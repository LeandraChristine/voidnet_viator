//Turns teensy-lc and psp-stick into a scroll & zoom device. Flash using USB-Type Keyboard + Mouse + Joystick.

#define deadzone 40 //+/- this value will not send a signal
#define offset 480 // compensation for the value on the stick in the neutral position
#define min_analog 120
#define max_analog 840
#define min_speed 0
#define max_speed 2

int analog_hor = A0;
int analog_ver = A1;
int hor = 0;  // variable to store the value read
int ver = 0;  // variable to store the value read

int normalizeInput(int val) {
  val = val - offset;

  if (val < deadzone && val >= -deadzone) {
    val = 0;
  }

  return val;
}

int rescale (int val) {
  int range_analog = max_analog - min_analog;
  int range_speed = max_speed - min_speed;
   
  float percent = (float)val / (float) range_analog * 2.0;
  
  float scaled_speed = percent * range_speed;
  //Serial.println(scaled_speed);
  return (int) scaled_speed;
}

void setup() {
  //Serial.begin(9600);           //  setup serial
  Keyboard.begin();
}

void loop() {
  hor = analogRead(analog_hor);  //signal from left/right tilt of stick
  ver = analogRead(analog_ver);  //signal from up/down tilt of stick

  int scroll_ver = rescale(normalizeInput(ver));
  if (scroll_ver != 0) Mouse.move(0,0,scroll_ver);

  int scroll_hor = rescale(normalizeInput(hor));
  if (scroll_hor != 0) {
    Keyboard.press(KEY_LEFT_CTRL);
    Mouse.move(0,0,scroll_hor);
    Keyboard.release(KEY_LEFT_CTRL);
  }
  delay(200); //larger delay feels like an indent when scrolling
}
