# PAST012-A
# max関数で大きい方選択するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

x, y, z = rm()
print(max(x+z, y))
