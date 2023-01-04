# 典型90-020
# logでなく整数処理でいける(誤差を考えなくてもよくなるし)
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b, c = rm()
if a < c**b:
    print('Yes')
else:
    print('No')
