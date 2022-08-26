# jsc2021-A
# math.ceilを使い数学的に実装
import sys
import math

rm = lambda: map(int, sys.stdin.readline().split())

x, y, z = rm()
print(math.ceil(z*y/x) - 1)
