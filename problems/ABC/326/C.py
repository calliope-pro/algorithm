# ABC326-C
# ある値からmを足した数がどの位置になるかを二分探索で求めるだけ
import bisect
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
al = rl()
al.sort()
ans = 0
for i in range(n):
    m_i = bisect.bisect_left(al, al[i] + m - 0.2)
    ans = max(ans, m_i - i)
print(ans)
