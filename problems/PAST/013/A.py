# PAST013-A
# 普通に切り捨て除算を使うだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, x, y = rm()
print(n//x * y)
