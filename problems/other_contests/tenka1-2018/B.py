# tenka1-2018-beginner-B
# 切り捨て除算を使うことで楽に実装
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b, k = rm()
for i in range(k):
    if i&1:
        b //= 2
        a += b
    else:
        a //= 2
        b += a
print(a, b)
