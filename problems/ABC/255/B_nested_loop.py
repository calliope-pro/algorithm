import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n, k = rm()
a = rl()
j = 0
li_a = []
li_b = []
for i in range(n):
    if a[j] == i+1:
        j = min(1+j, k-1)
        li_a.append(rl())
    else:
        li_b.append(rl())

ans = 0
for bv in li_b:
    tmp = inf
    for av in li_a:
        tmp = min(tmp, ((av[0]-bv[0])**2 + (av[1]-bv[1])**2)**0.5)
    ans = max(tmp, ans)
print(ans)
