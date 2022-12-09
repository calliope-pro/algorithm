# ABC280-A
# for文回して#の個数を数えるだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
ans = 0
for _ in range(h):
    ans += rr().count('#')
print(ans)
