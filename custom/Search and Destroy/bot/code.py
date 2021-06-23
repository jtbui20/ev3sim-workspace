import time
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B

x = int(input())
y = int(input())

print(f"Green X={x}")
print(f"Green Y={y}")

motor1 = LargeMotor(OUTPUT_A)
motor2 = LargeMotor(OUTPUT_B)

StartX = -50
StartY = 35

UnitsPerSecond = 26.316
SecondsPerUnit = 1.0 / UnitsPerSecond

goZero = False
Simple = False

if goZero:
    motor1.on_for_seconds(100, 1.9)
    motor2.on_for_seconds(100, 1.33)
    # Therefore horizontal is 50 / 1.9 = 26.316 units/second.
    # or 35 / 1.33 = 26.316 units/second.

else:
    # Find distance we need to travel
    DistanceX = abs(x - StartX)
    DistanceY = abs(y - StartY)
    print(f"Distance to travel right {DistanceX}")
    print(f"Distance to travel down {DistanceY}")

    if (Simple):
        motor1.on_for_seconds(100, DistanceX * SecondsPerUnit)
        # For 1D robots, rotate the robot here to face down.

        motor2.on_for_seconds(100, DistanceY * SecondsPerUnit)
    else:
        # Find ratio between
        RatioX = DistanceX / (DistanceX + DistanceY)
        RatioY = DistanceY / (DistanceX + DistanceY)
        print(f"Raw Speed Right {RatioX}")
        print(f"Raw Speed Down {RatioY}")
        
        # Set the largest value to 100, then push the lower one up
        if max(RatioX, RatioY) == RatioX:
            diff = 1 / RatioX
            RatioX = 1
            RatioY *= diff
        else:
            diff = 1 / RatioY
            RatioY = 1
            RatioX *= diff
        
        print(f"Max Speed Right {RatioX}")
        print(f"Max Speed Down {RatioY}")

        # Find direct time
        import math
        Time = math.sqrt(((DistanceX * SecondsPerUnit) ** 2) + (DistanceY * SecondsPerUnit) ** 2)
        print(Time)
        
        motor1.on_for_seconds(RatioX * 100, Time, block=False)
        motor2.on_for_seconds(RatioY * 100, Time)