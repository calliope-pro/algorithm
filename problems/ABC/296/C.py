# ABC296-C
# 問題読み間違えてて鬱。Counter使えば楽
import sys
import collections

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, x = rm()
al = rl()
counter = collections.Counter(al)
for v in counter:
    if counter[v - x] > 0 or counter[v + x] > 0:
        print('Yes')
        exit()
    counter[v] -= 1
print('No')
