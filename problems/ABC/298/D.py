# ABC298-D
# powで指数+余剰計算が強い。。。。
# dequeで数の変更を保持する
import sys
import collections

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))
mod2 = 998244353

q = ri()
s = 1
d = collections.deque([1])
for _ in range(q):
    qu = rl()
    if qu[0] == 1:
        s = (s*10 + qu[1]) % mod2
        d.append(qu[1])
    elif qu[0] == 2:
        n = d.popleft()
        s = (s - n*pow(10, len(d), mod2)) % mod2
    else:
        print(s)
