"""
7
6 2 4 1 3 5 7
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

n = ri()
li = rl()
#li = [a1, a2, ,,, , an]

queue = collections.deque([[1000000, 0]])

for i in range(n):
    c = li[i]
    while c >= queue[-1][0]:
        #pop()は末尾
        queue.pop()
    print(queue[-1][1])
    queue.append([c, i+1])