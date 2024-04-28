# ABC351-C
# deque使ってあとはシミュレーションするだけ
import collections
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
d = collections.deque()
for av in al:
    while len(d) and d[-1] == av:
        d_last = d.pop()
        av = d_last + 1
    d.append(av)
print(len(d))
