# ABC344-C
# O(NML)=10^6でとりあえず作れる数を作っておいて、それを使って判定する
import itertools
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
m = ri()
bl = rl()
l = ri()
cl = rl()
q = ri()
xl = rl()
xd = {}
for co in itertools.product(al, bl, cl):
    xd[sum(co)] = True
for xv in xl:
    if xd.get(xv, False):
        print("Yes")
    else:
        print("No")
