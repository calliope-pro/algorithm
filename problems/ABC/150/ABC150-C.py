'''
8
7 3 5 4 2 1 6 8
3 8 2 5 4 6 7 1
'''
import sys
import math
import itertools
import numpy

rl = sys.stdin.readline

r = int(rl())
n1 = tuple(map(int, rl().split()))
n2 = tuple(map(int, rl().split()))
li = list(itertools.permutations(range(1, r+1)))
print(abs(li.index(n1) - li.index(n2)))

