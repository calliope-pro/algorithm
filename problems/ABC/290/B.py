# ABC290-B
# 単純にfor-loopしてカウントと答え用に変数2つで管理
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

n, k = rm()
s = rr()
ans = ''
cnt = 0
for c in s:
    if c == 'o' and cnt < k:
        cnt += 1
        ans += 'o'
    else:
        ans += 'x'
print(ans)
