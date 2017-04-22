# BLE_Servo
Goal:

To create a framework to control a servo connected to an Arduino feather via bluetooth using Python from Linux. This is part of a larger project where the Arduino and servo will be attached to a drone for use for Techgarage game.


Materials:

Adafruit Feather 32u4 Bluefruit LE
https://learn.adafruit.com/adafruit-feather-32u4-bluefruit-le/overview

Small Servo Motor

Linux Computer (i.e Raspberry PI)

Bluetooth 4.0 USB Module (v2.1 Back-Compatible)
https://www.adafruit.com/product/1327


Setup:

1) Setup Arduino Feather https://learn.adafruit.com/adafruit-feather-32u4-bluefruit-le/assembly

2) Install Feather board support into IDE https://learn.adafruit.com/adafruit-feather-32u4-bluefruit-le/setup

3) Install the Adafruit nRF51 BLE Library https://learn.adafruit.com/adafruit-feather-32u4-bluefruit-le/installing-ble-library

4) Install BlueFruit Python libs on Linux machine https://learn.adafruit.com/bluefruit-le-python-library/installation

5) Connect servo to Arduino https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/the-breadboard-layout-for-sweep

6) Run list_uarts.py in Adafruit examples directory to find your Arduino's bluetooth addess. This value will be declared under the MYBLE variable in the autonomous2.py and the keycontrols.py programs. 


Files:

keycontrols.py - used as a framework for user keyboard input for servo.

autonomous2.py - starter framework for automous servo controls.

bluetooth_servo_arduino.zip - arduino bluetooth and servo sketch.


To Do:

Decide if the controls from Linux will be via keyboard or joystick

Test attached claw on drone to servo
