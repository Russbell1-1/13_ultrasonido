#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
Mi = Motor(Port.A)
Md = Motor(Port.D)
robot = DriveBase(Mi,Md, wheel_diameter=55.5, axle_track=104)
Sensor = UltrasonicSensor(Port.S2)
ev3.speaker.play_file("motor_start.wav")
while True:
    distancia = Sensor.distance()
    if distancia > 150:
        robot.drive(0,50)
        ev3.speaker.play_file("speed_down.wav")
        ev3.light.on(Color.GREEN)
    else: 
      acum = 0
      while acum < 2:
         ev3.light.on(Color.YELLOW)
         robot.stop()
         ev3.speaker.play_file("backing_alert.wav")
         acum += 1
      

      
      ev3.light.on(Color.YELLOW)
      wait(2000)

# Write your program here.

