# ABC352-A
# zがxとyの間にあるかどうかを判定する問題
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, x, y, z = rm()
if min(x, y) < z < max(x, y):
    print("Yes")
else:
    print("No")
