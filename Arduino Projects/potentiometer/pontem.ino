
int sensorPin = A0;  // including the pins according to each load
int ledPin = 8;      //A0 is an analogpin that can read information in more than two states
int ledPinx = 7;
void setup()
{
  pinMode(ledPin, OUTPUT);
  //pinMode(A0, INPUT);
}

void loop()
{
 
  int sensorV;
  // analog read Reads the value from the specified analog pin 
  sensorV = analogRead(sensorPin); // the specified pin is "sensorPin"
  digitalWrite(ledPin, HIGH);   // ledPin is turned on
  digitalWrite(ledPinx, HIGH);  // HIGH means turn on
  delay(sensorV);  // delay reading the next code for a value
  digitalWrite(ledPinx, HIGH); // turn on 
  digitalWrite(ledPin, LOW);   // LOW is to turn off   
  delay(sensorV); 
  
  
/* this lab uses three Leds
 one led is controlled by the pontentiometer and increases
 blinking according to the rotation of the resistor. 
 The second Led lights up to show the circuit functions.  
 The last Led shows the brightness being adjusted to 
 the potentiometer.  The pontentiometer works  having a resistive 
 element inside. Both end terminals are attached to it,
 and do not move. The wiper travels along the strip 
 when the knob is turned
                     */

  
}
