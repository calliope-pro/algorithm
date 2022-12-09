# ABC277-A
# str.index使うだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, x = rm()
p = rl()
print(p.index(x)+1)
