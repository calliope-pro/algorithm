# ABC274-A
# f-stringで桁指定するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
print(f'{b/a:.3f}')
