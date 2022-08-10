# ABC242-A
# 条件分岐
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b, c, x = rm()

if x <= a:
    print(1)
    exit()
if x > b:
    print(0)
    exit()
print(c / (b-a))
