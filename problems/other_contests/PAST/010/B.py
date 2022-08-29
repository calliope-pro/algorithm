# PAST010-B
# min関数使うだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b, x, y = rm()
print(min(x//a, y//b))
