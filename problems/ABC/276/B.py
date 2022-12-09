# ABC276-B
# 制約が緩いので、愚直に走査+最後にソートした
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
paths = [set() for _ in range(n)]
for _ in range(m):
    a, b = rm()
    paths[a-1].add(b)
    paths[b-1].add(a)
for path in paths:
    print(len(path), *sorted(path))
