# ABC331-A
# それぞれのy,m,dをうまく処理するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

M, D = rm()
y, m, d = rm()
ans = [0, 0, 1]
if d == D:
    m += 1
else:
    ans[2] = d+1

if m > M:
    ans[1] = m-M
    y += 1
else:
    ans[1] = m

print(y, ans[1], ans[2])
