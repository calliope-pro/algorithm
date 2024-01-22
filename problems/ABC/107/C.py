# ABC107-C
# dequeでk個を保持した
# その中で最も端にあるものを選び、所要時間を考える
import collections
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n, k = rm()
xl = rl()
d = collections.deque(xl[:k-1], maxlen=k)
ans = inf
for i in range(k-1, n):
    d.append(xl[i])
    if d[0]*d[-1] >= 0:
        ans = min(ans, max(abs(d[0]), abs(d[-1])))
    else:
        ans = min(ans, max(abs(d[0]), abs(d[-1])) + min(abs(d[0]), abs(d[-1]))*2)
print(ans)
