# ABC121-A
# やるだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
c, d = rm()
print((c-a) * (d-b))
