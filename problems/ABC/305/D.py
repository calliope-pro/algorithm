import bisect
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
acc = [0]
for i in range(n-1):
    if i+1 & 1:
        acc.append(acc[-1])
    else:
        acc.append(acc[-1] + al[i+1] - al[i])

q = ri()
for _ in range(q):
    l, r = rm()
    l_idx = bisect.bisect_left(al, l)
    r_idx = bisect.bisect_left(al, r)
    ans = 0
    if l_idx & 1 == 0:
        ans += al[l_idx] - l
    if r_idx & 1 == 0:
        ans += r - al[r_idx-1]
    print(ans + acc[r_idx-1] - acc[l_idx])
