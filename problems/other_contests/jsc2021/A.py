import sys
import math

rm = lambda: map(int, sys.stdin.readline().split())

x, y, z = rm()
print(math.ceil(z*y/x) - 1)
