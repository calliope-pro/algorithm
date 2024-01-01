# ABC321-B
# 条件分岐を工夫して3パターンに分ける
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, x = rm()
al = rl()
min_ = min(al)
max_ = max(al)
sum_ = sum(al)
if sum_ - max_ >= x:
    print(0)
    exit()
for i in range(min_, max_):
    if sum_ - min_ - max_ + i >= x:
        print(i)
        exit()
if sum_ - min_ >= x:
    print(max_)
    exit()
print(-1)
