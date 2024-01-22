# ABC313-B
# 弱いものを候補から落としていく
# 残ったものが答え候補
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
candidates = set(range(1, n+1))
for _ in range(m):
    a, b = rm()
    candidates.discard(b)
if len(candidates) != 1:
    print(-1)
else:
    print(candidates.pop())
