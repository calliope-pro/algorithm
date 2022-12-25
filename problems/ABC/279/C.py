# ABC279-C
# 列の構成要素が等しいかを判定するためにソートすればよい
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
s = [rr() for _ in range(h)]
t = [rr() for _ in range(h)]
s = sorted(zip(*s))
t = sorted(zip(*t))
print('NYoe s'[s == t::2])
