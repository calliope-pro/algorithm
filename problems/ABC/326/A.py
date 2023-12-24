# ABC326 - A
# 比較をするだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

x, y = rm()
if -3 <= y-x <= 2:
    print('Yes')
else:
    print('No')
