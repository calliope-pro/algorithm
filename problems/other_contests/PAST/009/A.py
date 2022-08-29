# PAST009-A
# シンプル条件分岐
import sys

rm = lambda: map(int, sys.stdin.readline().split())

H, W = rm()
h, w = rm()
if h >= H and w <= W:
    print('Yes')
else:
    print('No')
