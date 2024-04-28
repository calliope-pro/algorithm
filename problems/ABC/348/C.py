# ABC348-C
# それぞれの色について最小のコストを記録しておく
import collections
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
inf = float("inf")

n = ri()
d = collections.defaultdict(lambda: inf)
for _ in range(n):
    a, c = rm()
    d[c] = min(d[c], a)
print(max(d.values()))
