# ABC352-C
# 最大のdiffを求めればあとは足すだけ
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
max_diff = 0
ans = 0
for _ in range(n):
    a, b = rm()
    ans += a
    max_diff = max(max_diff, b-a)
print(ans+max_diff)
