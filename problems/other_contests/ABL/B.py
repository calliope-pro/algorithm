# ABL-B
# 条件分岐するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b, c, d = rm()
if a<=b<c<=d or c<=d<a<=b:
    print('No')
else:
    print('Yes')
