# ABC318-A
# 数学的に解ける, ただしminに注意
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, m, p = rm()
print(max(0, (n - m) // p + 1))
