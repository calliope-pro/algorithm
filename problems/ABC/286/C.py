# ABC286-C
# 制約が小さいので、単純に2重ループさせればいい
# sを2分割するのはだるいので、あらかじめ2倍にしておくことで楽になる
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())
inf = float('inf')

n, a, b = rm()
s = rr()
s = s*2
ans = inf
for i in range(n//2 + 1):
    tmp = i*a
    for c1, c2 in zip(s[i:i+n//2], reversed(s[i+n//2:i+n])):
        if c1 != c2:
            tmp += b
    ans = min(tmp, ans)
print(ans)
