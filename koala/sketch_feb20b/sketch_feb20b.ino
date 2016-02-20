#include <ArduinoRobot.h> // include the robot library

void setup() {
  // put your setup code here, to run once:
  Robot.begin();
  Robot.beginTFT();

  // Robot.lineFollowConfig(14, 9, 50, 10);
  
  //set the motor board into line-follow mode
  // Robot.setMode(MODE_LINE_FOLLOW);  

  Robot.text("Start", 5, 5);
}

void loop() {
  // put your main code here, to run repeatedly:
  Robot.updateIR(); // update the IR array
  if (Robot.IRarray[0] && Robot.IRarray[1] && Robot.IRarray[2] && Robot.IRarray[3] && Robot.IRarray[4])
    Robot.motorsWrite(25,25);//Make the robot go forward, full speed
  if (Robot.IRarray[0] && Robot.IRarray[1])
    Robot.motorsWrite(-25,25);//Make the robot rotate left, full speed
  if (Robot.IRarray[3] && Robot.IRarray[4])
    Robot.motorsWrite(25,-25);//Make the robot rotate right, full speed
  if (Robot.IRarray[2])
    Robot.motorsWrite(25,25);//Make the robot go forward, full speed
  if (Robot.IRarray[1])
    Robot.motorsWrite(25,25);
  if (Robot.IRarray[3])
    Robot.motorsWrite(25,25);
  if (Robot.IRarray[4])
    Robot.motorsWrite(-25,25);
  if (Robot.IRarray[0])
    Robot.motorsWrite(25,-25);
  if (Robot.IRarray[1] && Robot.IRarray[2] && Robot.IRarray[3])
    Robot.motorsWrite(25,25);//Make the robot go forward, full speed
  if (!Robot.IRarray[0] && !Robot.IRarray[1] && !Robot.IRarray[2] && !Robot.IRarray[3] && !Robot.IRarray[4])
    Robot.motorsStop(); //Make the robot stop
}
