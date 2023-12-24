# ABC317-A
# ソート済みなのでbisect.bisect_leftを使うと脳死で解ける
import bisect
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, h, x = rm()
pl = rl()
print(bisect.bisect_left(pl, x-h) + 1)
