# Week 1 diagnostic: Python checks
import math

print(round((1.7 - 0.5) / 2, 4), round((1.4 - 0.2) / 0.6, 4))                  # 1, 2
print([round(math.radians(d), 4) for d in (90, 45, 30)], round(math.degrees(1), 1))  # 3
print(round(math.hypot(0.3, 0.4), 4), round(math.degrees(math.atan(0.3 / 0.4)), 2))  # 4, 5
x, y = 1 + 3, 2 + (-1)
print(x, y, round(math.hypot(x, y), 2))                                          # 6
print((49 - 44) / (54 - 44) * 100, round(0.25 * math.sin(math.radians(30)), 4))  # 7, 8
f = lambda x: 3 * x - 2
print(f(4), (10 + 2) / 3)                                                        # 9
