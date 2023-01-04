# ABC002-B
# collections.Counterを使うと楽
import sys
import collections

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
c = collections.Counter(s)
print(c.most_common(1)[0][0])
