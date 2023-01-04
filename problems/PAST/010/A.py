# PAST010-A
# min, max関数使うだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b, c = rm()
print(min(a*b, b*c, c*a), max(a*b, b*c, c*a))
