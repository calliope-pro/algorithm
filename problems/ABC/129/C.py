# ABC129-C
# フィボナッチ数列と気付けるか
# 後は条件分岐をしっかりとするだけ
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
mod1 = 10**9 + 7

n, m = rm()
li = set(ri() for _ in range(m))
a, b = 1, 1 if 1 not in li else 0
for i in range(2, n+1):
    a, b = b, a+b if i not in li else 0
    a %= mod1
    b %= mod1
print(b)
