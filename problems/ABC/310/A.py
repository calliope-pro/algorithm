# ABC310-A
# minを使えば余裕
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, p, q = rm()
dl = rl()
print(min(p, min(dl) + q))
