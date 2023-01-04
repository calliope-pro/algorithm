# PAST008-C
# .count組み込みメソッド使うだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, x = rm()
a = rl()
print(a.count(x))
