# キーエンスプログラミング コンテスト2020-B
# 貪欲法
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
se = []
for _ in range(n):
    x, r = rm()
    start, end = x-r, x+r
    se.append([start, end])
se.sort(key=lambda x: x[1])

cur = se[0][0]
cnt = 0
for i in se:
    if cur <= i[0] <= i[1]:
        cur = i[1]
        cnt += 1
print(cnt)


