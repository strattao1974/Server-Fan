#include <dht11.h>

dht11 DHT11;
#define dhtpin 7
#define relay 10
float temp;

void setup(){
  pinMode(dhtpin,INPUT);
  pinMode(relay,OUTPUT);  
  Serial.begin(9600);
}

void loop(){
  delay(1000);
  DHT11.read(dhtpin);
  temp = DHT11.temperature;
  Serial.print(temp);
  Serial.println("C    ");

  if(temp>=30)                   // Turn the fan on
  {
    digitalWrite(relay,LOW);
    //Serial.println(relay);
  }
  else                          // Turn the fan off
  {
    digitalWrite(relay,HIGH);
    //Serial.println(relay);
   }
}
