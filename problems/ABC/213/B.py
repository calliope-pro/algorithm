# ABC213-B
# マルチソートするのだ
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
a = rl()
a = [(v, i) for i, v in enumerate(a)]
a.sort()
print(a[-2][1] + 1)
