# ABC303-B
# 制約が小さいので、ペアが存在してるか逐一検証した
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
s = set(c for c in itertools.combinations(range(1, n+1), r=2))
for _ in range(m):
    a = rl()
    for c in zip(a, a[1:]):
        s.discard(tuple(sorted(c)))
print(len(s))
