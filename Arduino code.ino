//L293D
//Motor A
const int motorPin1  = 5; 
const int motorPin2  = 6;  
//Motor B
const int motorPin3  = 9; 
const int motorPin4  = 10 ;
char serialData;


void setup(){
    
    pinMode(motorPin1, OUTPUT);
    pinMode(motorPin2, OUTPUT);
    pinMode(motorPin3, OUTPUT);
    pinMode(motorPin4, OUTPUT);  
    Serial.begin(9600);
   
}


void loop(){
   serialData=Serial.read();
    if(serialData=='w')
    {
    analogWrite(motorPin1,255);
    analogWrite(motorPin2,0);
    analogWrite(motorPin3,255);
    analogWrite(motorPin4,0);
     
    }
    if(serialData=='a')
    {
    analogWrite(motorPin1,170);
    analogWrite(motorPin2,0);
    analogWrite(motorPin3,255);
    analogWrite(motorPin4,0)
        }
    if(serialData=='d')
    {
    analogWrite(motorPin1,255);
    analogWrite(motorPin2,0);
    analogWrite(motorPin3,170);
    analogWrite(motorPin4,0)
      
    }
    if(serialData=='s')
    {
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    digitalWrite(motorPin3, LOW);
    digitalWrite(motorPin4, LOW);
    }  
    if(serialData=='c')
    {
    analogWrite(motorPin1,255);
    analogWrite(motorPin2,0);
    analogWrite(motorPin3,0);
    analogWrite(motorPin4,0)
   
    }
    if(serialData=='z')
    {
    analogWrite(motorPin1,0);
    analogWrite(motorPin2,0);
    analogWrite(motorPin3,255);
    analogWrite(motorPin4,0)
     
    }
}
