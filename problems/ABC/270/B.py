# ABC270-B
# 条件分岐をしっかりと。。こういう問題だるい。
import sys

rm = lambda: map(int, sys.stdin.readline().split())

x, y, z = rm()
if x * y < 0 or abs(x) < abs(y):
    print(abs(x))
    exit()
if z * y < 0:
    print(abs(z)*2 + abs(x))
    exit()
if abs(z) < abs(y):
    print(abs(x))
else:
    print(-1)
