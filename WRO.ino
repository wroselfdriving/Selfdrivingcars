#include <Servo.h>
#define in1 6
#define in2 7
#define in3 8
#define in4 9
#define en1 5
#define en2 10

#define led1 0
#define led2 1
#define led3 2
#define led4 4
#define led5 11
#define led6 12
Servo my_servo; 


char cmmd; 

void Forward(int S)
{
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(en1, S);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(en2, S);
}



void setup() {
  // put your setup code here, to run once:
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  Serial.begin(9600);
  pinMode(en1, OUTPUT);
  pinMode(en2, OUTPUT);

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  my_servo.attach(3);
}

void loop(){
  while (!Serial.available());
  cmmd = Serial.read();
  
  

  if(cmmd == 'F'){Forward(100);Serial.print("Forward");}
  if(cmmd == 'B'){Forward(100);Serial.print("Backward");}
  if(cmmd == 'R'){Forward(100);Serial.print("Right");}
  if(cmmd == 'L'){Forward(100);Serial.print("Left");}
  }
 
