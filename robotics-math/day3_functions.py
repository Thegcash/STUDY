# Day 3: function notation

def f(x):
    return 3 * x - 2

def g(t):
    return 0.2 * t      # hand position (m) after t seconds

# Problem 1: forward, put x in
print(f(0), f(4))

# Problem 2: backward, undo in reverse (add 2, then divide by 3)
print((10 + 2) / 3, (-5 + 2) / 3)

# Problem 3: forward, then backward (undo x0.2 by dividing)
print(g(5), 1.4 / 0.2)

# Retry: practice problems solved by hand after missing 2 and 3
print(
    (6 + 4) / 2,     # 2x - 4 = 6    -> 5
    (-7 + 3) / 4,    # 4x - 3 = -7   -> -1  (same type I missed)
    3 / 0.5,         # 0.5t = 3      -> 6 s
    0.2 * 4,         # g(4)          -> 0.8 m
    1.8 / 0.2,       # 0.2t = 1.8    -> 9 s
    (21 - 1) / 4,    # 4x + 1 = 21   -> 5
    (-2 + 6) / 2,    # 2x - 6 = -2   -> 2
)
