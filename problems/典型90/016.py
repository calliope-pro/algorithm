# 典型90-016
# PyPy only
# でかい金額順にコイン数を決定させると計算量を効率的に落とせる
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')

n = ri()
al = rl()
al.sort(reverse=True)
a, b, c = al
ans = inf
for cnt_a in range(n//a, -1, -1):
    r = n - a*cnt_a
    for cnt_b in range(r//b, -1, -1):
        r_ = r - b*cnt_b
        if r_ % c == 0 and r_ >= 0:
            ans = min(r_//c + cnt_a + cnt_b, ans)
            break
print(ans)