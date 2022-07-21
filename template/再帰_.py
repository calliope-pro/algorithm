# ABC166 C
import sys

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
rsl = lambda: list(sys.stdin.readline().split())
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rf = lambda: map(float, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod1 = 10**9 + 7
# mod2 = 

n = ri()
h_li = rl()
def f(h):
    if all([i == 0 for i in h]):
        return 0
    elif all([i != 0 for i in h]):
        return f([i-1 for i in h]) + 1
    else:
        zero_idx = h.index(0)
        return f(h[:zero_idx]) + f(h[zero_idx+1:])
        
print(f(h_li))
            




















