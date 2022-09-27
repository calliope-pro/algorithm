# PAST011-C
# 単調増加であること、10**9以降はコストが掛かることを考慮すればいいだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, m = rm()
border = 10**9
ans = ''
for i in range(1, m+1):
    if n**i <= border:
        ans += 'o'
    else:
        ans += 'x' * (m - len(ans))
        break
print(ans)
