# ABC086-C
# ループと条件分岐をしっかりと行いシミュレーションする
# 前の点から到着可能かを判定
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
t_prev, x_prev, y_prev = 0, 0, 0
for _ in range(n):
    t_now, x_now, y_now = rm()
    t_diff = t_now - t_prev
    x_diff = abs(x_now - x_prev)
    y_diff = abs(y_now - y_prev)
    if t_diff&1 != (x_diff + y_diff)&1:
        print('No')
        exit()
    if t_diff < x_diff + y_diff:
        print('No')
        exit()
    t_prev, x_prev, y_prev = t_now, x_now, y_now
print('Yes')
