import sys
import collections

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
c = collections.Counter(s)
for k, v in c.items():
    if v == 1:
        print(k)
        exit()
print(-1)
