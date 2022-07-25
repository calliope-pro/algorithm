"""
8 11
0 3 1
0 1 5
0 2 4
1 4 2
2 4 5
2 3 2
2 5 6
4 7 1
4 6 3
5 6 2
6 7 4
"""
import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.buffer.readline().rstrip()
rs = lambda: sys.stdin.buffer.readline().split()
ri = lambda: int(sys.stdin.buffer.readline())
rm = lambda: map(int, sys.stdin.buffer.readline().split())
rl = lambda: list(map(int, sys.stdin.buffer.readline().split()))

n, m = rm()
li = [[] for _ in range(m)]
for _ in range(m):
    a, b, time = rm()
    li[a].append([b, time])
    li[b].append([a, time])

dist = [1000] * n
dist[0] = 0
seen = []
todo = collections.deque([0])
while todo:
    for next_city in li[todo[0]]:
        nc = next_city[0]
        if nc not in seen:
            if nc not in todo:
                todo.append(nc)
            if dist[nc] > dist[todo[0]] + next_city[1]:
                dist[nc] = dist[todo[0]] + next_city[1]
    else:
        seen.append(todo[0])
        todo.popleft()

print(dist)


