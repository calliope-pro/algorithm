# ABC343-A
# 0~10のsetからa+bを除いたものを1つpopで出力する
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
s = set(range(0, 10))
s.discard(a+b)
print((set(range(0,10))-{a+b}).pop())
