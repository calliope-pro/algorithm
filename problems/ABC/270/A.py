# ABC270-A
# 1, 2, 4という数字に着目してOR演算をすると速い
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
print(a | b)
