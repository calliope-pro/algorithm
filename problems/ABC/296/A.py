# ABC296-A
# 含有されてるかチェックするだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
print('YNeos'[('MM' in s or 'FF' in s)::2])
