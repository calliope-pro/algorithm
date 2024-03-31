# ABC343-C
# 立方数なので10^18ではなく10^6くらいまで探せばいい
import math
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
for i in range(math.floor((n+100)**(1/3)), 0, -1):
    i3 = i**3
    if i3 > n:
        continue
    if str(i3) == str(i3)[::-1]:
        print(i3)
        break
