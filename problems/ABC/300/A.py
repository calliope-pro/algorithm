# #ABC300-A
# Aにしては面倒な方
# 計算して、該当するインデックス + 1
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, a, b = rm()
cl = rl()
print(cl.index(a+b) + 1)
