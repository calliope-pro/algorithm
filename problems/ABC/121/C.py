# ABC121-C
# 安いやつから貪欲的に買う。それだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
cnt = 0
cnt_money = 0
for i in sorted(rl() for _ in range(n)):
  a, b = i
  if cnt + b < m:
    cnt += b
    cnt_money += a*b
  else:
    cnt_money += (m - cnt) * a
    break
print(cnt_money)
