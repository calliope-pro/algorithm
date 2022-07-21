import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, m, x, t, d = rm()
if m > x:
    print(t)
else:
    print(t - (x-m) * d)
