# ABC329-C
# groupbyを使うととても楽
import sys
import itertools

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
d = {}
for c, t in itertools.groupby(s):
    d[c] = max(d.get(c, 0), len(tuple(t)))
print(sum(d.values()))
