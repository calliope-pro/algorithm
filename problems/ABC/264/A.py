# ABC264-A
# slice使うだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

l, r = rm()
print('atcoder'[l-1:r])
