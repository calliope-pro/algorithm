# ABC121-D
# 偶数の次の奇数とのxorは1になることを利用
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
ans = 0
if a & 1:
    a_ = a+1
    ans ^= a
else:
    a_ = a

if b & 1:
    b_ = b
else:
    b_ = b-1
    ans ^= b
ones = ((b_ + 1 - a_) // 2) % 2
print(ans ^ ones)
