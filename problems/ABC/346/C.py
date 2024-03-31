# ABC346-C
# 1~kの和から条件に合うaに含まれる数を引けばいい
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, k = rm()
as_ = set(v for v in rm() if v <= k)
print((1+k)*k//2 - sum(as_))
