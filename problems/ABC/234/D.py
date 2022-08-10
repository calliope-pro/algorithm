# ABC234-D
# heapを使う
import sys
import heapq

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
p = rl()
h = p[:k]
heapq.heapify(h)
print(h[0])
for v in p[k:]:
    if h[0] < v:
        heapq.heappushpop(h, v)
    print(h[0])
