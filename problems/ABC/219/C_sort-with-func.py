import sys

rr = lambda: sys.stdin.readline().rstrip()
rsl = lambda: list(sys.stdin.readline().rstrip())
ri = lambda: int(sys.stdin.readline())

x = rsl()
d = {}
for i, xv in enumerate(x):
    d[xv] = i
n = ri()
s = [rr() for _ in range(n)]
s.sort(key=lambda x: tuple(d[xc[0]] for xc in x))
print('\n'.join(s))
