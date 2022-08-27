# ABC266-E
# N回目の試行では、N-1回目の期待値より低いものは期待値で試行し、高いものはそのままの値を用いる
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
ans = 3.5
for _ in range(1, n):
    l = int(ans)
    ans = (ans*(l) + sum(range(l+1, 7))) / 6
print(ans)
