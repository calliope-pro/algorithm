# ABC014-C
# 単純ないもす法だ。楽しい
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
imos = [0] * 1000002
for _ in range(n):
    a, b = rm()
    imos[a] += 1
    imos[b+1] -= 1
ans = 0
tmp = 0
for v in imos:
    tmp += v
    ans = max(tmp, ans)
print(ans)
