# ABC302-A
# ceilと同じことだけど精度優先で実装した
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
print(-(-a // b))
