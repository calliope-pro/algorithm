# ABC298-A
# 含有を調べるだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
if 'o' in s and 'x' not in s:
    print('Yes')
else:
    print('No')
