import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n, q = rm()
p = list(range(0, n))
v = list(range(0, n))

for _ in range(q):
    vl = ri() - 1
    pl = p[vl]
    if pl == n-1:
        pr = pl - 1
    else:
        pr = pl + 1
    vr = v[pr]

    v[pl], v[pr] = vr, vl
    p[vl], p[vr] = pr, pl
print(*(i+1 for i in v), sep=' ')
