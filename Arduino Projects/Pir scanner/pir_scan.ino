int led = 13;
int sensor = 2;  // coonection of pins to load 
int led2 = 7;
int pirstate = LOW;  // the nital state of the pir 
void setup() {
  pinMode(led, OUTPUT);   // to output information to the user 
  pinMode(sensor, INPUT);
  Serial.begin(9600); // calling the serial monitor 
}
void loop() {
  int sensorval = digitalRead(sensor);  // new int that calls to sensor 
  Serial.println(sensorval);
 
  if (sensorval == HIGH) {   // if the sensor is off
    digitalWrite(led, HIGH);  // the red led is on
    digitalWrite(led2, LOW);   // blue led is off
    
  }
  else {                         // else 
    if (sensorval == LOW) {  // if the sensor is high
    digitalWrite(led, LOW);   // red led is off
    digitalWrite(led2, HIGH);  // blue led is on 
    
}  
}
}
/* furthur observations:
a serial monitor is a screen that displays information 
of what is happening in the circuit and certain ints can be 
displayed.  Pir scanner works by using the infared light
radiated by objects entering the range.
*/
