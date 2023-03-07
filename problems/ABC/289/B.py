# ABC289-B
# 返り点があった際はtmpリストにappendして
# 返り点がない時はtmpを逆順に出力
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
a_set = set(rl())
tmp = []
for i in range(1, n+1):
    if i in a_set:
        tmp.append(i)
    else:
        print(i, *tmp[::-1], end=' ')
        tmp = []
