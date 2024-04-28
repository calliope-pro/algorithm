# ABC350-B
# すべて1のリストを作って、toggleするだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, q = rm()
tl = rl()
l = [1] * n
for tv in tl:
    l[tv - 1] = 1 - l[tv - 1]
print(sum(l))
