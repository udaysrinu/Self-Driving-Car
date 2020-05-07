//this is arduino code with uses IR sensors
void setup()
{
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  //pinMode(13, OUTPUT);
}
void loop()
{
  int a = analogRead(A0);
  int b = analogRead(A1);
  int c = analogRead(A2);
  if (a > 800 && b < 800 && c > 800)
  { analogWrite(5, 250);
    analogWrite(6, 0);
    analogWrite(10, 250);
    analogWrite(11, 0);
    Serial.println("Forward condition true");
  }
  else if (a < 500 && b < 500 && c > 800)
  { analogWrite(5, 0);
    analogWrite(6, 250);
    analogWrite(10, 250);
    analogWrite(11, 0);
    Serial.println(" sudden left condition true");
    delay(200);
  }
  else if (a > 800 && b < 800 && c < 800)
  { analogWrite(5, 250);
    analogWrite(6, 0);
    analogWrite(10, 0);
    analogWrite(11, 250);
    Serial.println("sudden right condition true");
    delay(200);
  }
  else if (a > 800 && b > 800 && c < 800)
  { analogWrite(5, 200);
    analogWrite(6, 0);
    analogWrite(10, 0);
    analogWrite(11, 0);
    Serial.println("slightright condition true");
  }
  else if (a < 800 && b > 800 && c > 800)
  { analogWrite(5, 0);
    analogWrite(6, 0);
    analogWrite(10, 200);
    analogWrite(11, 0);
    Serial.println("slightleft condition true");
  }
}
