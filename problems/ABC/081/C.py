# ABC081-C
# collections.Counterを利用する
# 少ないものを順に選べばいい
import sys
import collections

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
a = rl()
c = collections.Counter(a)
print(sum(sorted(c.values(), reverse=True)[k:]))
