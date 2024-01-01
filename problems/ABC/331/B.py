# ABC331-B
# 制約が小さいので全探索できる
import sys

rm = lambda: map(int, sys.stdin.readline().split())
inf = float('inf')

n, s, m, l = rm()
ans = inf
for i in range(50):
    for j in range(50):
        for k in range(50):
            if 6*i + 8*j + 12*k >= n:
                ans = min(ans, i*s + j*m + k*l)
print(ans)
