# ABC069-A
# 分割数は点の数より1少ない。
# あとはやるだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
print((a-1)*(b-1))
