# ABC141-D
# heapq
import sys
import math
import heapq

rs = lambda: sys.stdin.readline().split()
rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
h = list(map(lambda x: -1*int(x), rs()))
heapq.heapify(h)
for _ in range(m):
    heapq.heappushpop(h, math.ceil(h[0]/2))
print(-sum(h))