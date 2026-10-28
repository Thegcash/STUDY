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
