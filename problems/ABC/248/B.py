# ABC248-B
# 指数関数になるので、適当にループした回数出せばいいい
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b, k = rm()

for i in range(10000000000000):
    if a >= b:
        print(i)
        break
    a *= k
