# ABC327 - A
# sが短いので愚直に探索するだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
if 'ab' in s or 'ba' in s:
    print('Yes')
else:
    print('No')
