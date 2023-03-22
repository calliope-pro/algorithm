# ABC294-C
# 単調増加 -> にぶたんでいい！
import bisect
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
al = rl()
bl = rl()
for i, av in enumerate(al, 1):
    j = bisect.bisect_left(bl, av)
    print(i+j, end=" ")
print()
for i, bv in enumerate(bl, 1):
    j = bisect.bisect_left(al, bv)
    print(i+j, end=" ")
