import time
from typing import ForwardRef
from ev3dev2.motor import LargeMotor
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3sim.code_helpers import CommandSystem

topMotor = LargeMotor("outA")
botMotor = LargeMotor("outB")
color = ColorSensor("in1")
ultrasonic = UltrasonicSensor("in2")

# Here's some helper functions to reduce some of the trial and error.
# Jump to the bottom of the file to seem how to use them.

def wait():
    time.sleep(0.1)

def rotate(neg):
    # rotate(1): clockwise 90 degrees.
    # rotate(-1): counterclockwise 90 degrees.
    topMotor.on_for_seconds(neg * 10, 1.6, block=False)
    botMotor.on_for_seconds(-neg * 10, 1.6)
    wait()

def forward():
    botMotor.on_for_seconds(20, 1.9, block=False)
    topMotor.on_for_seconds(20, 1.9)
    wait()

# Let's copy paste the instructions ...

# Green Wall    |  RLLLLLLL...
# Red Wall      |  LLRLLR...
# Blue Wall     |  RRLLRRLL...
# Green No Wall |  FFF...
# Red No Wall   |  LRLRLR...
# Blue No Wall  |  FRFRFR...

# ... and let the robot know what they are

gwi = ["R", "L"]
rwi = ["L", "L", "R"]
bwi = ["R", "R", "L", "L"]
gni = ["F"]
rni = ["L", "R"]
bni = ["F", "R"]

# Let's make some counters
gw = 0
rw = 0
bw = 0
gn = 0
rn = 0
bn = 0

pword = ""

while True:
    r, g, b = color.rgb
    DistanceToWall = ultrasonic.distance_centimeters
    if DistanceToWall <= 5: isWall = True
    else: isWall = False
    
    if r + g + b >= 300:
        break
    elif r >= 200:
        pword += "R"
        if isWall:
            if rwi[rw] == "L":
                rotate(-1)
                forward()
            else:
                rotate(1)
                forward()
            if rw == 2:
                rw = 0
            else:
                rw += 1
        else:
            if rni[rn] == "L":
                rotate(-1)
                forward()
            else:
                rotate(1)
                forward()
            if rn == 1:
                rn = 0
            else:
                rn += 1
    elif g >= 200:
        pword += "G"
        if isWall == True:
            if gw == 0:
                rotate(1)
                forward()
                gw += 1
            else:
                rotate(-1)
                forward()
        else:
            forward()
    elif b >= 200:
        command = ""
        pword += "B"
        if isWall:
            command = bwi[bw]
            if bw == 3:
                bw = 0
            else:
                bw += 1
        else:
            command = bni[bn]
            if bn == 1:
                bn = 0
            else:
                bn += 1
        if command == "F":
            forward()
        elif command == "L":
            rotate(-1)
            forward()
        elif command == "R":
            rotate(1)
            forward()
    else:
        break

    print(pword)


print(f"Password is {pword}")
CommandSystem.send_command(CommandSystem.TYPE_CUSTOM, pword)
