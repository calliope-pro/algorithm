# ABC285-A
# 二分木の性質をしっかりと見る
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
if b == a*2 or b == a*2 + 1:
    print('Yes')
else:
    print('No')
