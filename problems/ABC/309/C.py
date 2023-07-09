# ABC309-C
# いもす法と座圧。
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, k = rm()
d = {}
sum_ = 0
for _ in range(n):
    a, b = rm()
    sum_ += b
    d[a] = d.get(a, 0) - b
if sum_ <= k:
    print(1)
    exit()
for day in sorted(d.keys()):
    sum_ += d[day]
    if sum_ <= k:
        print(day+1)
        exit()
