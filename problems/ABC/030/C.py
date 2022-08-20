# ABC030-C
# 二分探索を用いて愚直にシミュレーション
import bisect
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
x, y = rm()
a = rl()
b = rl()
idx_a = 0
idx_b = -1
is_a2b = True
t = a[0]
cnt = 0
while True:
    if is_a2b:
        is_a2b = False
        t += x
        idx_b = max(bisect.bisect_left(b, t), idx_b+1)
        if idx_b >= m:
            break
        t = b[idx_b]
    else:
        is_a2b = True
        t += y
        idx_a = max(bisect.bisect_left(a, t), idx_a+1)
        cnt += 1
        if idx_a >= n:
            break
        t = a[idx_a]
print(cnt)
