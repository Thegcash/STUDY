# Day 4: degrees and radians
import math

def deg_to_rad(d):
    return d * math.pi / 180

def rad_to_deg(r):
    return r * 180 / math.pi

# Problem 1: 180, 90, 45, 30 degrees -> radians
print([round(deg_to_rad(d), 4) for d in (180, 90, 45, 30)])

# Problem 2: 1 radian -> degrees
print(round(rad_to_deg(1), 1))

# Problem 3: G1 elbow at 1.2 rad -> degrees
print(round(rad_to_deg(1.2), 1))

# Retry: practice problems from my test
print(
    round(rad_to_deg(2), 1),      # 2 rad    -> 115 deg
    round(rad_to_deg(3.14), 1),   # 3.14 rad -> 180 deg (half a turn)
    round(deg_to_rad(60), 3),     # 60 deg   -> 1.047 rad (I first said 1)
    round(rad_to_deg(10)),        # 10 rad   -> 573 deg: past a full turn, bad sensor reading
)
