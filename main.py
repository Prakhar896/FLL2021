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

### testing begin
# # Write your program here.
# ev3.speaker.beep()

# # Run motor b for 500 degrees
# test_motor = Motor(Port.B)
# test_motor.run_target(500, 90)

# # Play another beep sound.
# ev3.speaker.beep(frequency=1000, duration=500)
### testing end

