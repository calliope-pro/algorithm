# ABC315-B
# 中間までの日を計算して、貪欲的に探すだけ
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

m = ri()
dl = rl()
mid = (sum(dl) + 1) // 2
s_ = 0
for a, d in enumerate(dl, 1):
    if s_ + d >= mid:
        print(a, mid - s_)
        exit()
    s_ += d
