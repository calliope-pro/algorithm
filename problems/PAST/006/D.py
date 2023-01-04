# PAST006-D
# 典型的な累積和
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
a = rl()
cum = [0] + list(itertools.accumulate(a))
for i in range(n-k+1):
    print(cum[i+k] - cum[i])
