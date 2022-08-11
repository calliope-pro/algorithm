# ABC256-D
# いもす法
# 起点と終点の判定をflagで管理
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
li = [0]*2*10**5
for _ in range(n):
    l, r = rm()
    li[l-1] += 1
    li[r-1] += -1

sum_ = 0
start = 0
flag = False
for idx, v in enumerate(li, 1):
    sum_ += v
    if sum_ > 0 and not flag:
        start = idx
        flag = True
    if sum_ <= 0 and flag:
        print(start, idx)
        flag = False
