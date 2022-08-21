import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
a = rl()
b = rl()
print(*sorted(set(a) ^ set(b)))
