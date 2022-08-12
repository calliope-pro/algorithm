# ABC221-D
# いもす法をリスト不使用で算出する
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
imos = []
for _ in range(n):
    av, bv = rm()
    imos.append((av, 1))
    imos.append((av + bv, -1))
imos.sort()
d = [0] * (n+1)
cnt = 1
last = imos[0][0]
for v, delta in imos[1:]:
    d[cnt] += v - last
    last = v
    cnt += delta
print(*d[1:])
