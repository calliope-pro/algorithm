'''
6 9
0 1 1
0 2 3
1 2 1
1 3 7
2 4 1
1 4 3
3 4 1
3 5 1
4 5 6
'''
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

v, e = rm()

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

li = []
for _ in range(e):
    s, t, w = rm()
    li.append([w, s-1, t-1]) #wを先頭にした
else:
    #wでsortしやすい
    li = heapsort(li)

r = [0] * v
par = list(range(v))
def root(x):
    #親、根の特定
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def same(x, y):
    #共通根があるか
    return root(x) == root(y)

def union(x, y):
    #根の結合,ランク
    x = root(x)
    y = root(y)
    if x != y:
        if r[x] == r[y]:
            r[x] += 1
            par[y] = x
            return
        elif r[x] > r[y]:
            par[y] = x
            return
        else:
            par[x] = y
    return

def kruskal(edges):
    #クラスカル法による最小全域木
    res = 0
    for i in edges:
        w, s, t = i
        if not same(s, t):
            res += w
            union(s, t)
    else:
        return res

print(kruskal(li))