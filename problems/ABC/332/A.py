# ABC332 - A
# 数回queryとって計算するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, s, k = rm()
cost = 0
for _ in range(n):
    p, q = rm()
    cost += p*q
if cost < s:
    cost += k
print(cost)
