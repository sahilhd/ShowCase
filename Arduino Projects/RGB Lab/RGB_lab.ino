int redPin = 11;   // setting the arduino pins according to the loads
int greenPin = 10;
int bluePin = 9;
int redLed = 4;
int buttonOnpin = 6;
int buttonOffpin = 3;
void setup()
{ // pinmode is used to notify what that pin will do 
  pinMode(redPin, OUTPUT);  // OUTPUT is using pin for outputting information which is colour
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(buttonOnpin, INPUT_PULLUP); /* input pullup is using the pin 
  and load to input information to other parts of the circuit 
  as it is taking in information */
}

void loop()
{
  if(digitalRead(buttonOnpin) == LOW)  // if the button is off 
  
  {
   digitalWrite(redLed, HIGH);  // led is on 
   
    setColor(255,0,0); //red tab
    delay(5000); // the user will have 5 seconds to execute the task
    setColor(0,255,0); //green tab
    delay(5000);
    setColor(0,0,255); //blue tab
    //delay(5000);
  }
  
  if(digitalRead(buttonOffpin) == LOW) // the button is off
    
  {
    digitalWrite(redLed, LOW); //led is off
  }
  
  
}
void setColor(int red, int green, int blue)
{
#ifdef COMMON_ANODE     // calling from the library
  
red = 255 - red;      // this section will allow to slowly move to colours
green = 255 - green;
blue = 255 - blue;
#endif
analogWrite(redPin, red);  // to read the infromation of the analog pins
analogWrite(greenPin, green);
analogWrite(bluePin, blue);
  
/* this lab shows the transition of 
colours to red to blue with buttons
RGB led works by having smaller red, blue , green
leds that can have the brightness adjusted of each smaller
led to make different colours.  
SInce brightness has to be adjusted 
PMW waves are used.
*/
  
}
