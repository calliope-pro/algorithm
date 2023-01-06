# 典型90-038
# Python only
# Pythonだからオーバーフロー考えずに突っ込めばいい
import sys
import math

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
print('Large' if (c := a // math.gcd(a, b) * b) > 10**18 else c)
