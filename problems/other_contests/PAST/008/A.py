# PAST008-A
# min関数で簡略化
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b, c, d = rm()
print(min(a+b-c, d))
