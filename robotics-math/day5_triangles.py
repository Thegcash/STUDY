# Day 5: right triangles and the robot arm
import math

def height(L, angle_deg):
    return L * math.sin(math.radians(angle_deg))   # up: opposite side -> sin

def reach(L, angle_deg):
    return L * math.cos(math.radians(angle_deg))   # forward: side touching the angle -> cos

# Problem 1: Pythagoras
print(round(math.sqrt(0.6**2 + 0.8**2), 3))
# Problem 2-4
print(round(height(0.25, 30), 3), round(reach(0.25, 30), 3), round(height(0.3, 45), 3))

# Retry: practice after mixing up sin and cos
print(
    round(height(0.4, 30), 3),    # 0.2   (half the arm at 30 deg)
    round(reach(0.4, 30), 3),     # 0.346
    round(height(0.2, 45), 3),    # 0.141
    round(reach(0.5, 30), 3),     # 0.433
    round(height(0.8, 60), 3),    # 0.693
    round(reach(0.4, 60), 3),     # 0.2   (I first used 0.866 here)
    round(math.sqrt(1 + 1), 2),   # 1.41  hypotenuse of a 1-1 triangle = sqrt(2)
)
