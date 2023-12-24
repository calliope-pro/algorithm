# ABC313-A
# 1番目の人がすでに最強の場合を考えていなかった。。。
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
pl = rl()
if max(pl) == pl[0] and pl.count(pl[0]) == 1:
    print(0)
    exit()
print(max(pl) - pl[0] + 1)
