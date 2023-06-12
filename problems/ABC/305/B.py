import sys
import itertools

rs = lambda: sys.stdin.readline().split()

l = [0, 3, 1, 4, 1, 5, 9]
l = list(itertools.accumulate(l))
p, q = sorted(rs())
print(l[ord(q)-65] - l[ord(p)-65])
