# ABC281-C
# 合計値を計算し、余りを使うことで楽になる
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, t = rm()
a = rl()
sum_ = sum(a)
t %= sum_
for i, av in enumerate(a):
    t -= av
    if t < 0:
        print(i+1, t+av)
        exit()
