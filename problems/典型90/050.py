# 典型90-050
# 漸化式を考えるだけ。フィボナッチ数列の派生。
# lru_cacheだとダメだった(泣)
import sys

rm = lambda: map(int, sys.stdin.readline().split())
mod1 = 10**9 + 7

n, l = rm()
steps = [1] * l
for i in range(n-l+1):
    steps.append((steps[-1]+steps.pop(0)) % mod1)
print(steps[-1])
