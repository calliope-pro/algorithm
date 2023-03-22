# ABC294-A
# ループと、偶奇判定
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
for av in al:
    if not av & 1:
        print(av, end=' ')
