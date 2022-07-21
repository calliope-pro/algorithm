# ABC007 C
import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
from functools import reduce
from string import ascii_lowercase, ascii_uppercase
from queue import Queue
import time

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
rsl = lambda: list(sys.stdin.readline().split())
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rf = lambda: map(float, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod1 = 10**9 + 7
# mod2 = 
al = ascii_lowercase
au = ascii_uppercase

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

q = Queue()
h, w = rm()
sy, sx = rm()
gy, gx = rm()
c = [rr() for _ in range(h)]
m = np.full([h, w], -1)
m[sy-1, sx-1] = 0
q.put([sy-1, sx-1])

while not q.empty():
    y, x = q.get()
    for dy, dx in zip(dys, dxs):
        if 0 <= y + dy < h and 0 <= x + dx < w:
            if c[y+dy][x+dx] == '.' and m[y+dy, x+dx] == -1:
                q.put([y+dy, x+dx])
                m[y+dy, x+dx] = m[y, x] + 1
                print(m)
                time.sleep(1)
print(m[gy-1, gx-1])
                    
    

    


