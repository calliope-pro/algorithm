# ABC263-A
# Counterも用いた
import sys
import collections

rl = lambda: list(map(int, sys.stdin.readline().split()))

c = list(collections.Counter(rl()).values())
c.sort()
print('YNeos'[c!=[2,3]::2])
