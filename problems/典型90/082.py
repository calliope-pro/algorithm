# 典型90-082
# 文字列と数字の特徴の規則性を上手く活かす
# 10**nが要となる
import sys

rm = lambda: map(int, sys.stdin.readline().split())
mod1 = 10**9 + 7

l, r = rm()
len_l = len(str(l))
len_r = len(str(r))
if len_l == len_r:
    print(((l + r) * (r - l + 1) * len_l // 2) % mod1)
    exit()
ans = (10**(len_r - 1) + r) * (r - 10**(len_r - 1) + 1) * len_r // 2
for i in range(len_l, len_r):
    ans += (10**i - 1 + l) * (10**i - l) * i // 2
    ans %= mod1
    l = 10**i
print(ans)
