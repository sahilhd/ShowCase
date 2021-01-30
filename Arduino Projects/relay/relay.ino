int relay = 3;
int ReadPin = 0;

void setup() {   
  pinMode(relay, OUTPUT);
    pinMode(ReadPin, INPUT);
    Serial.begin(9600);
}
void loop() {  
  digitalWrite(relay, HIGH);   
  delay(analogRead(ReadPin) * 5);      
  digitalWrite(relay, LOW);
  delay(analogRead(ReadPin) * 5);
}
/* diode function of a diode is to allow an electric
  current to pass in one direction 
  while blocking it in the opposite direction 
  (the reverse direction).  Moving the current foward from the
  terminal to the next.  Relays are switches that open 
  and close circuits electromechanically or electronically. 
  Relays control one electrical circuit by opening and 
  closing contacts in another circuit. 
  Transitors work by turning a small input current into a large output 
  current, the transistor acts like an amplifier. 
  But it also acts like a switch at the same time.  Flow moves
  between two different locations.
  
  */
  
