

#include <LiquidCrystal.h> // calling from the library 



LiquidCrystal lcd(12,11,5,4,3,2);  // what pins will be used 

void setup()
{


  lcd.begin(16, 2); // calling the lcd


  lcd.clear();

  

  

  lcd.print("Hi Mrs.Stewart"); // text printed 

}

void loop()
{


  lcd.setCursor(0,1); // set pins for the cursor 

  
}

/* the pixels are switched on or off electronically
using liquid crystals to rotate polarized light.  Made of 
polarized glass a back light projects the image.*/
