# ABC278-A
# 条件分岐するより制約が小さいため愚直にループさせた
import sys
import collections

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
a = collections.deque(rl())
for _ in range(k):
    a.popleft()
    a.append(0)
print(*a)
