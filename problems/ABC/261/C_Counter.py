import sys
import collections

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
c = collections.Counter()
for _ in range(n):
    s = rr()
    if c[s] > 0:
        print(f'{s}({c[s]})')
    else:
        print(s)
    c[s] += 1
