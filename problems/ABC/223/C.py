# ABC223-C
# 中間点は時間が半分であることに気付く
# nが10^5 -> ナイーブにシミュレートすればいい(わざわざ二分探索しなくていい)
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
ab = [rl()for _ in range(n)]
time = 0
for a, b in ab:
    time += a/b

time /= 2
time_ = 0
length = 0
for a, b in ab:
    tmp = time_ + a/b
    if time_ <= time <= tmp:
        print(length + (time - time_)*b)
        exit()
    time_ = tmp
    length += a
