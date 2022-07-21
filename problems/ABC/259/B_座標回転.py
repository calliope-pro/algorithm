import sys
import math

rm = lambda: map(int, sys.stdin.readline().split())

a, b, d = rm()

theta = math.atan2(b, a)
theta += math.radians(d)
print((a**2 + b**2)**0.5 * math.cos(theta), (a**2 + b**2)**0.5 * math.sin(theta))
