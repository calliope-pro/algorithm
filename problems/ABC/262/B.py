# ABC262-B
# 制約が少ないため、全探索すれば楽(一応setで含まれるかの計算量を減らした)
import sys
import itertools

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
s = set()
for _ in range(m):
    u, v = rm()
    s.add((u, v))

ans = 0
for i, j, k in itertools.product(range(1, n+1), repeat=3):
    if i < j < k and (i, j) in s and (j, k) in s and (i, k) in s:
        ans += 1
print(ans)
