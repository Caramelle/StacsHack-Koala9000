#include <Wire.h>
#include <ArduinoRobot.h> // include the robot library

long timerOrigin; // used for counting elapsed time

void setup() {
  // initialize the Robot, SD card, display, and speaker 
  Robot.begin();
  Robot.beginTFT();
  Robot.beginSD();
  Robot.beginSpeaker();

  // show the logots on the TFT screen
  
  Robot.drawBMP("lf.bmp", 0, 0); // display background image

 // Robot.playFile("chase.sqm");  // play a song from the SD card
  
  // add the instructions
  Robot.text("Line Following\n\n place the robot on\n the track and \n see it run", 5, 5);
  Robot.text("Press the middle\n button to start...", 5, 61);
  Robot.waitContinue();

  // These are some general values that work for line following 
  // uncomment one or the other to see the different behaviors of the robot
  //Robot.lineFollowConfig(10, 10, 10, 5);
  Robot.lineFollowConfig(14, 9, 50, 10);
  
  //set the motor board into line-follow mode
  Robot.setMode(MODE_LINE_FOLLOW);  
  
  // start
  Robot.fill(255, 255, 255);
  Robot.stroke(255, 255, 255);
  Robot.rect(0, 0, 128, 80); // erase the previous text
  Robot.stroke(0, 0, 0);
  Robot.text("Start", 5, 5);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  Robot.updateIR(); // update the IR array
  if (Robot.IRarray[0] && Robot.IRarray[1] && Robot.IRarray[2] && Robot.IRarray[3] && Robot.IRarray[4]){
    Robot.motorsWrite(25,25);//Make the robot go forward, full speed
    delay(200);
  }
  else if (Robot.IRarray[1] && Robot.IRarray[2] && Robot.IRarray[3]){
    Robot.motorsWrite(25,25);//Make the robot go forward, full speed
    delay(200);
  }
  else if (Robot.IRarray[0] && Robot.IRarray[1] && Robot.IRarray[2]){
    Robot.motorsWrite(2, 4);//Make the robot rotate right, full speed
    delay(200);
  }
  else if (Robot.IRarray[2] && Robot.IRarray[3] && Robot.IRarray[4]){
    Robot.motorsWrite(4, 2);
    delay(200);
  }
  else if (Robot.IRarray[1] && (Robot.IRarray[0] || Robot.IRarray[2])){
    Robot.motorsWrite(3, 5);//Make the robot rotate right, full speed
    delay(200);
  }
  else if (Robot.IRarray[3] && (Robot.IRarray[4] || Robot.IRarray[2])){
    Robot.motorsWrite(5, 3);//Make the robot rotate left, full speed
    delay(200);
  }
  else if (Robot.IRarray[2]){
    Robot.motorsWrite(25,25);//Make the robot go forward, full speed
    delay(200);
  }
  else if (Robot.IRarray[1] || Robot.IRarray[0]){
    Robot.motorsWrite(3, 10);
    delay(200);
  }
  else if (Robot.IRarray[3] || Robot.IRarray[4]){
    Robot.motorsWrite(10, 3);
    delay(200);
  }
  else if (!Robot.IRarray[0] && !Robot.IRarray[1] && !Robot.IRarray[2] && !Robot.IRarray[3] && !Robot.IRarray[4]){
    Robot.motorsStop(); //Make the robot stop
    delay(200);
  }
}
