# ABC213-A
# xorするだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
print(a^b)
