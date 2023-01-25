# ABC090-C
# 実際に何通りかで確かめてみるといい
# コーナーケースに注意して条件分岐する
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
if n*m == 1:
    print(1)
elif n == 1 or m == 1:
    print(n*m - 2)
else:
    print((n-2) * (m-2))
