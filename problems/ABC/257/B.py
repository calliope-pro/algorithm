# ABC257-B
# しっかりと問題を読み、シミュレーションするだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k, q = rm()
a = rl()
l = rl()
for lv in l:
    if a[lv-1] != n:
        if lv == k:
            a[lv-1] += 1
        elif a[lv] != a[lv-1] + 1:
            a[lv-1] += 1
print(*a)
