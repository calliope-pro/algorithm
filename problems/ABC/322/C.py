# ABC322-C
# 貪欲的にみていく。indexの管理できていればOK
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
al = rl()
al_i = 0
for i in range(n):
    if i+1 < al[al_i]:
        print(al[al_i] - i - 1)
    if i+1 == al[al_i]:
        al_i += 1
        print(0)
