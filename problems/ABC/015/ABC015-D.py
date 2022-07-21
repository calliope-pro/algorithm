# unsolved
import sys
import math
import itertools
import collections
import numpy as np

rl = sys.stdin.readline
n = int(rl())
s = rl()
cnt = 1
for i in range(n-1):
  if s[i] != s[i+1]:
    cnt += 1
print(cnt)
  
