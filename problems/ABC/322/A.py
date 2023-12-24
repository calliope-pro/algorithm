# ABC322-A
# 文字列探索するだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
if 'ABC' not in s:
    print(-1)
    exit()
print(s.index('ABC') + 1)
