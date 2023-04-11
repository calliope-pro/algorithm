# ABC297-A
# インデックス使って前後の判断と、for-break-elseを使うだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, d = rm()
tl = rl()
for i in range(n-1):
    if tl[i+1] - tl[i] <= d:
        print(tl[i+1])
        break
else:
    print(-1)
