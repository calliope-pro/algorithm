# PAST013-D
# 単純にシミュレーションするだけ、0-+で共通の処理はまとめた
import sys

rsl = lambda: list(sys.stdin.readline().rstrip())
rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
sl = rsl()
tmp = 0
cnt = [0] * n
for i, sv in enumerate(sl):
    cnt[i%n] += 1
    if sv == '-':
        tmp += cnt[i%n]
        cnt[i%n] = 0
    if sv == '+':
        cnt[i%n] += tmp
        tmp = 0
print(*cnt, sep='\n')
