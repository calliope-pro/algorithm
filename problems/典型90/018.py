# 典型90-018
# 俯角はatan2使えばいい。数学計算しっかりとしよう。
import sys
import math

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

t = ri()
l, x, y = rm()
q = ri()
for _ in range(q):
    e = ri()
    theta = e*2*math.pi/t
    h = (l/2) * (1 - math.cos(theta))
    w = math.sqrt(x**2 + (y + (l/2) * math.sin(theta))**2)
    print(math.degrees(math.atan2(h, w)))
